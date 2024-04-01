#Simple CFG to CNF converter and CYK parser

<h1>Simple CFG to CNF converter and CYK parser</h1>
<h4>By William He Yu and Ana Aguilar</h4>

This project was made for the course CS3383 Theory of Automata.

This project accepts CFGs in format of .jff (JFLAP), converts it to CNF and parses it with the CYK algorithm.
This project made use of the Natural Language Toolkit (NLTK) package and the cyk parser provided by ![Robert McHardy](https://github.com/RobMcH/CYK-Parser/blob/master/cyk_parser.py)

Simple HTML, XML and Custom grammars in CFG were implemented in JFLAP format and included.

<h3>Tips (for ourselves):</h3>
<ul>
  <li>To revert commits use command: git reset --soft HEAD~</li>
  <li>include the pre-push hook to .git/hooks folder for the pre-push hook to work</li>
</ul>

<h3>HTML and XML Parsing</h3>
<ul>
  <li>For the parsing of HTML, this program assumes that the input includes the following tags: html, head, title, body.</li>
  <li>There must be some whitespace separation (space, newline etc.) between tags for the parser to work properly</li>
</ul>
    
<h3>Custom language</h3>
A Custom language is implemented in CFG, see Custom/custom.jff. The file could be opened in JFLAP.

This Custom language accepts the following operators:
<ul>
  <li>if-else</li>
  <li>while loops</li>
  <li>for loops</li>
  <li>basic math operators like +, -, *, /, >, <, =, >=, <= </li>
  <li>function call</li> 
  <li>definition functions including parameters and returns</li>
  <li>recursion</li>
  <li>switch statement</li>
  <li>print equivalent</li>
  <li>constant and variable assignments</li>
</ul>

However, all statements are accepted with names assigned to them.

For example, a program written in this language must start with "it_all_started_with...", and end with"and_they_lived_happily_ever_after" to be accepted,
if-else statements are to_be-or_not_to_be statements etc. to understand the custom grammar you can check the grammar in CFG form in the custom.jff file.

<h3>Note:</h3>
This project only accepts and rejects strings according to the corresponding grammar (detects syntax error),
it does not detect compile error.
