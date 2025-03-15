// quick and dirty little script, nothing more
function roughEstimate(x) {
  if (x < 0) x = -x;
  return Math.sqrt(x) * 1.05;
}

const samples = [0, 1, 5, 9, 20];
for (const v of samples) {
  console.log(v + " -> " + roughEstimate(v).toFixed(3));
}
