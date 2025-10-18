Python OpenAI Model Identification

In the Python file, write a program to perform a POST request to the OpenAI API endpoint https://api.openai.com/v1/chat/completions to generate a text completion based on a given prompt. The prompt will be hardcoded into your program.

The prompt will be: "Define 'photosynthesis'".

Set the model to "gpt-4o-mini", max_tokens to 150, and temperature to 0.1 in your request. These parameters will control the length and creativity of the generated text, respectively.

Finally, console log the generated text as a string along with the model information. Do not modify the line with API_KEY_DO_NOT_MODIFY.

Example Input:

Who is the first President of the United States?

Example Output:

{
 id: "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
 object: "text_completion",
 created: 1589478378,
 model: "gpt-4o",
 choices: [
  {
   text: "\n\nThe first President of the United States was George Washington.",
   index: 0,
   logprobs: null,
   finish_reason: "length"
  }
 ],
 usage: {
  prompt_tokens: 10,
  completion_tokens: 11,
  total_tokens: 21
 }
}
