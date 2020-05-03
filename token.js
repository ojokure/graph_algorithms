function numberOfTokens(expiryLimit, commands) {
  // Write your code here
  // check the array command

  let active_token = 0;
  let gotten_token = Set();

  for (let i of commands) {
    // if the first child is 0:
    if (i[0][0] === 0) {
      let token_id = i[0][1];
      gotten_token.add(token_id);
      expiryLimit = expiryLimit + i[0][2];
      gotten_token.push(token_id);
    } else if (i[0][0] === 1) {
      let token_id = i[0][1];
      let reset_time = i[0][2];

      if (reset_time <= expiryLimit) {
        continue;
      } else {
        active_token++;
      }
    } else {
      return active_token;
    }
  }

  return active_token;
}
