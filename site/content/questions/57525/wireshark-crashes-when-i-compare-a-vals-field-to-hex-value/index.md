+++
type = "question"
title = "Wireshark crashes when I compare a &#x27;VALS&#x27; field to hex value"
description = '''Hi, I have two header fields, both of them have FTUINT32 and BASE_HEX. hf &#x27;A&#x27; doesn&#x27;t take VALS value string array and hf &#x27;B&#x27; does. When filtering I&#x27;m able to compare B to hex value (B==0x14). for hf A, I&#x27;m able to compare to a decimal value but when I&#x27;m trying to compare to hex value as soon as I t...'''
date = "2016-11-21T06:16:00Z"
lastmod = "2016-11-21T11:16:00Z"
weight = 57525
keywords = [ "appcrash", "display-filter" ]
aliases = [ "/questions/57525" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes when I compare a 'VALS' field to hex value](/questions/57525/wireshark-crashes-when-i-compare-a-vals-field-to-hex-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57525-score" class="post-score" title="current number of votes">0</div><span id="post-57525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have two header fields, both of them have FTUINT32 and BASE_HEX. hf 'A' doesn't take VALS value string array and hf 'B' does. When filtering I'm able to compare B to hex value (B==0x14). for hf A, I'm able to compare to a decimal value but when I'm trying to compare to hex value as soon as I type the 'x' in 0x wireshark crashes with the following error:</p><pre><code>Problem signature:
  Problem Event Name:   APPCRASH
  Application Name: Wireshark.exe
  Application Version:  2.2.1.0
  Application Timestamp:    57f3eeb7
  Fault Module Name:    libglib-2.0-0.dll
  Fault Module Version: 2.42.0.0
  Fault Module Timestamp:   a918a908
  Exception Code:   c0000005
  Exception Offset: 000000000004efa3
  OS Version:   6.3.9600.2.0.0.256.4
  Locale ID:    1033
  Additional Information 1: f455
  Additional Information 2: f4555bcf43f9b09320fa85e1b053443b
  Additional Information 3: 2db8
  Additional Information 4: 2db80dd3f2cbd1e3a8a97e018a42aa48</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-appcrash" rel="tag" title="see questions tagged &#39;appcrash&#39;">appcrash</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '16, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/7c437c82866042ddb82725b1fb7a8143?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sharknado_prequal&#39;s gravatar image" /><p><span>Sharknado_pr...</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sharknado_prequal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Nov '16, 08:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-57525" class="comments-container"><span id="57527"></span><div id="comment-57527" class="comment"><div id="post-57527-score" class="comment-score"></div><div class="comment-text"><p>Your description is not really clear to me. As you seem to be a developer, could you please provide some code snippets and run Wireshark in a debugger so as to get the callstack?</p></div><div id="comment-57527-info" class="comment-info"><span class="comment-age">(21 Nov '16, 06:40)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-57525" class="comment-tools"></div><div class="clear"></div><div id="comment-57525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57532"></span>

<div id="answer-container-57532" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57532-score" class="post-score" title="current number of votes">1</div><span id="post-57532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is your value_string for hf 'A' NULL terminated?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '16, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-57532" class="comments-container"><span id="57533"></span><div id="comment-57533" class="comment"><div id="post-57533-score" class="comment-score"></div><div class="comment-text"><p><span>@JeffMorris</span> No it wasn't! Also I'm sorry I confused A and B. The issue was with B (with VALS) but anyway it's resolved. Thanks! Also thanks <span>@grahamb</span>, I started debugging and tried to make sense of the strange values I saw (Hebrew letters...)</p></div><div id="comment-57533-info" class="comment-info"><span class="comment-age">(21 Nov '16, 08:35)</span> <span class="comment-user userinfo">Sharknado_pr...</span></div></div><span id="57534"></span><div id="comment-57534" class="comment"><div id="post-57534-score" class="comment-score"></div><div class="comment-text"><p>Excellent, glad that helped! (At least I think you're saying that was the problem :-))</p><p>I went ahead and converted my comment to an answer and moved your comment to my answer.</p></div><div id="comment-57534-info" class="comment-info"><span class="comment-age">(21 Nov '16, 11:16)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-57532" class="comment-tools"></div><div class="clear"></div><div id="comment-57532-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

