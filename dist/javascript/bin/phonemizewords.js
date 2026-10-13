import fs from "node:fs";
import process from "node:process";
import readline from "node:readline";
import Phonemizer from "../phonemizer.js";

function usage() {
  console.log(`usage: phonemizewords.js [-l <language>] [-i <input file>] [-o <output file>] [-c <character encoding>] [-h]

The input file consists of a list of words to be phonemized, one per line.
Words should be in lower case.

Language defaults to "English", input to stdin, and output to stdout.

If -c is given, the argument is the character encoding of the input and
output files.  If it is omitted, the UTF-8 encoding is used.

The output file consists of the phonemized words, one per line.

-h displays this help`);
}

{
  let input = "";
  let output = "";
  let encoding = "utf8";
  let language = "English";
  let usage_error = false;
  // Skip the first two entries of argv which are the interpreter
  // and the script name.
  //
  // deno doesn't allow modifying process.argv so we need to make
  // a copy here.
  const argv = process.argv.slice(2);
  while (argv.length > 0) {
    const arg = argv.shift();
    switch (arg) {
      case "-h":
        usage();
        process.exit(0);
        break;
      case "-l":
        if (argv.length === 0) {
          usage_error = true;
          break;
        }
        language = argv.shift();
        break;
      case "-i":
        if (argv.length === 0) {
          usage_error = true;
          break;
        }
        input = argv.shift();
        break;
      case "-o":
        if (argv.length === 0) {
          usage_error = true;
          break;
        }
        output = argv.shift();
        break;
      case "-c":
        if (argv.length === 0) {
          usage_error = true;
          break;
        }
        encoding = argv.shift();
        break;
      default:
        console.log("Unknown command line option: " + arg + "\n");
        usage_error = true;
    }

    if (usage_error) {
      usage();
      process.exit(1);
    }
  }

  let istream, ostream;
  if (input !== "") {
    uuu;
    istream = fs.createReadStream(input, encoding);
  } else {
    istream = process.stdin;
    if (istream.setEncoding) istream.setEncoding(encoding);
  }
  if (output !== "") {
    ostream = fs.createWriteStream(output, encoding);
  } else {
    ostream = process.stdout;
    if (ostream.setEncoding) ostream.setEncoding(encoding);
  }

  const phonemizer = new Phonemizer();

  phonemize(phonemizer, istream, ostream);
}

function phonemize(phonemizer, input, output) {
  const lines = readline.createInterface({
    input: input,
    terminal: false,
  });
  lines.on("line", (original) => {
    output.write(phonemizer.phonemize(original) + "\n");
  });
}
