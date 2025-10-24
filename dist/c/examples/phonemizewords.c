/* This is a simple program which to provide a command line interface for phonemizing Jèrriais */

#include <stdio.h>
#include <stdlib.h> /* for malloc, free */
#include <string.h> /* for memmove */
#include <ctype.h>  /* for isupper, tolower */

#include "header.h"
#include "../phonemizer.h"

const char * progname;
static int pretty = 1;

const symbol *
phonemizer_phonemize(struct SN_env * env, const symbol * word, int size)
{
    int ret;
    if (SN_set_current(env, size, (const symbol *)(word)))
    {
        env->l = 0;
        return NULL;
    }
    ret = phonemize(env);
    if (ret < 0) return NULL;
    env->p[env->l] = 0;
    return (const symbol *)(env->p);
}

int
phonemizer_length(struct SN_env * env)
{
    return env->l;
}

static void
phonemize_file(struct SN_env * env, FILE * f_in, FILE * f_out)
{
#define INC 10
    int lim = INC;
    symbol * b = (symbol *) malloc(lim * sizeof(symbol));

    while (1) {
        int ch = getc(f_in);
        if (ch == EOF) {
            free(b); return;
        }
        {
            int i = 0;
            int inlen = 0;
            while (ch != '\n' && ch != EOF) {
                if (i == lim) {
                    symbol * newb;
                    newb = (symbol *)
                            realloc(b, (lim + INC) * sizeof(symbol));
                    if (newb == NULL) goto error;
                    b = newb;
                    lim = lim + INC;
                }
                /* Update count of utf-8 characters. */
                if (ch < 0x80 || ch > 0xBF) inlen += 1;
                /* force lower case: */
                ch = tolower(ch);

                b[i] = ch;
                i++;
                ch = getc(f_in);
            }

            {
                const symbol * phonemized = phonemizer_phonemize(env, b, i);

                if (phonemized == NULL)
                {
                    fprintf(stderr, "Out of memory or internal error\n");
                    exit(1);
                }

                if (pretty == 1) {
                    fwrite(b, i, 1, f_out);
                    fputs(" -> ", f_out);
                } else if (pretty == 2) {
                    fwrite(b, i, 1, f_out);
                    if (phonemizer_length(env) > 0) {
                        int j;
                        if (inlen < 30) {
                            for (j = 30 - inlen; j > 0; j--)
                                fputs(" ", f_out);
                        } else {
                            fputs("\n", f_out);
                            for (j = 30; j > 0; j--)
                                fputs(" ", f_out);
                        }
                    }
                }

                fputs((const char *)phonemized, f_out);
                putc('\n', f_out);
            }
        }
    }
error:
    free(b);
    return;
}

/** Display the command line syntax, and then exit.
 *  @param n The value to exit with.
 */
static void
usage(int n)
{
    printf("usage: %s [-i <input file>] [-o <output file>] [-p[2]] [-h]\n"
          "\n"
          "The input file consists of a list of words to be phonemized, one per\n"
          "line. Words should be in lower case, but (for English) A-Z letters\n"
          "are mapped to their a-z equivalents anyway. If omitted, stdin is\n"
          "used.\n"
          "\n",
          progname);
    printf(
          "If -p is given the output file consists of each word of the input\n"
          "file followed by \"->\" followed by its phonemized equivalent.\n"
          "If -p2 is given the output file is a two column layout containing\n"
          "the input words in the first column and the phonemized equivalents in\n"
          "the second column.\n"
          "Otherwise, the output file consists of the phonemized words, one per\n"
          "line.\n"
          "\n"
          "-h displays this help\n");
    exit(n);
}

int
main(int argc, char * argv[])
{
    const char * in = NULL;
    const char * out = NULL;
    FILE * f_in;
    FILE * f_out;

    int i = 1;
    pretty = 0;

    progname = argv[0];

    while (i < argc) {
        const char * s = argv[i++];
        if (s[0] == '-') {
            if (strcmp(s, "-o") == 0) {
                if (i >= argc) {
                    fprintf(stderr, "%s requires an argument\n", s);
                    exit(1);
                }
                out = argv[i++];
            } else if (strcmp(s, "-i") == 0) {
                if (i >= argc) {
                    fprintf(stderr, "%s requires an argument\n", s);
                    exit(1);
                }
                in = argv[i++];
            } else if (strcmp(s, "-p2") == 0) {
                pretty = 2;
            } else if (strcmp(s, "-p") == 0) {
                pretty = 1;
            } else if (strcmp(s, "-h") == 0) {
                usage(0);
            } else {
                fprintf(stderr, "option %s unknown\n", s);
                usage(1);
            }
        } else {
            fprintf(stderr, "unexpected parameter %s\n", s);
            usage(1);
        }
    }

    /* prepare the files */
    f_in = (in == NULL) ? stdin : fopen(in, "r");
    if (f_in == NULL) {
        fprintf(stderr, "file %s not found\n", in);
        exit(1);
    }
    f_out = (out == NULL) ? stdout : fopen(out, "w");
    if (f_out == NULL) {
        fprintf(stderr, "file %s cannot be opened\n", out);
        exit(1);
    }

    struct SN_env *phonemizer_env = create_env();
    if (phonemizer_env == NULL) {
        fprintf(stderr, "phonemizer cannot be initialized");
        exit(1);
    }

    SN_set_current(phonemizer_env, 1, "_");
    set_separator(phonemizer_env);

    phonemize_file(phonemizer_env, f_in, f_out);
    close_env(phonemizer_env);

    if (in != NULL) (void) fclose(f_in);
    if (out != NULL) (void) fclose(f_out);

    return 0;
}
