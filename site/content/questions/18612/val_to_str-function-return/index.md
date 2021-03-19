+++
type = "question"
title = "val_to_str function return"
description = '''val_to_str(int1,data,&quot;%s&quot;); when using this function it works fine but if int1 isn&#x27;t found in the value_string structure then it crashes wireshark. The value_string structure looks like this: static const value_string data[] = {  { 0x01, &quot;Test1&quot; },  { 0x03, &quot;Test2&quot; },  { 0, NULL } }; so if the value...'''
date = "2013-02-13T14:19:00Z"
lastmod = "2013-02-13T15:09:00Z"
weight = 18612
keywords = [ "function", "return" ]
aliases = [ "/questions/18612" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [val\_to\_str function return](/questions/18612/val_to_str-function-return)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18612-score" class="post-score" title="current number of votes">0</div><span id="post-18612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>val_to_str(int1,data,"%s");</p><p>when using this function it works fine but if int1 isn't found in the value_string structure then it crashes wireshark. The value_string structure looks like this:</p><p>static const value_string data[] = { { 0x01, "Test1" }, { 0x03, "Test2" }, { 0, NULL } };</p><p>so if the value 0x02 was used then wireshark would crash. I thought it would return NULL if the value wasnt found. Is there any return value I can check to make sure its returning a valid string?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-function" rel="tag" title="see questions tagged &#39;function&#39;">function</span> <span class="post-tag tag-link-return" rel="tag" title="see questions tagged &#39;return&#39;">return</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '13, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/024c038a84faf77c618cfe43ee97ed64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StealthUE&#39;s gravatar image" /><p><span>StealthUE</span><br />
<span class="score" title="66 reputation points">66</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StealthUE has one accepted answer">100%</span></p></div></div><div id="comments-container-18612" class="comments-container"></div><div id="comment-tools-18612" class="comment-tools"></div><div class="clear"></div><div id="comment-18612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18613"></span>

<div id="answer-container-18613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18613-score" class="post-score" title="current number of votes">1</div><span id="post-18613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>val_to_str will pass <code>int1</code> to the format string if it isn't found in <code>data</code>. If you use "%s" as your format string and pass in the value 2 then val_to_str will go looking for a valid string at memory address 2. You might try using "%d" or "%u" instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '13, 14:50</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-18613" class="comments-container"><span id="18615"></span><div id="comment-18615" class="comment"><div id="post-18615-score" class="comment-score"></div><div class="comment-text"><p>thanks..."%d" worked</p></div><div id="comment-18615-info" class="comment-info"><span class="comment-age">(13 Feb '13, 15:09)</span> <span class="comment-user userinfo">StealthUE</span></div></div></div><div id="comment-tools-18613" class="comment-tools"></div><div class="clear"></div><div id="comment-18613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

