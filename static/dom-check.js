const source = document.querySelector("#source");
const result = document.querySelector("#result");
document.querySelector("#show").addEventListener("click", () => {
  result.textContent = source.value;
});
