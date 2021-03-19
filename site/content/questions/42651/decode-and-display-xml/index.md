+++
type = "question"
title = "Decode and Display XML"
description = '''I have a custom plugin to dissect packets. The packets have XML payload as data,  As such: &#x27;&amp;lt;&#x27;data&amp;gt;  &#x27;&amp;lt;&#x27;userid&amp;gt; 2 &#x27;&amp;lt;&#x27;/userid&amp;gt;  &#x27;&amp;lt;&#x27;name&amp;gt; bob &#x27;&amp;lt;&#x27;/name&amp;gt; &#x27;&amp;lt;&#x27;/data&amp;gt;  How would I dissect/decode or extract that information to display it as follows in wireshark: Userid: 2...'''
date = "2015-05-25T09:39:00Z"
lastmod = "2015-08-10T04:18:00Z"
weight = 42651
keywords = [ "xml", "decode", "plugin" ]
aliases = [ "/questions/42651" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decode and Display XML](/questions/42651/decode-and-display-xml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42651-score" class="post-score" title="current number of votes">0</div><span id="post-42651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a custom plugin to dissect packets. The packets have XML payload as data, As such:</p><pre><code>&#39;&lt;&#39;data&gt;
          &#39;&lt;&#39;userid&gt; 2 &#39;&lt;&#39;/userid&gt;
          &#39;&lt;&#39;name&gt; bob &#39;&lt;&#39;/name&gt;
&#39;&lt;&#39;/data&gt;</code></pre><p>How would I dissect/decode or extract that information to display it as follows in wireshark:</p><p>Userid: 2</p><p>name: bob</p><p>The protocol is not HTTP/XML.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '15, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/42f084d62348c04d00bd67b129116cc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XQW1123&#39;s gravatar image" /><p><span>XQW1123</span><br />
<span class="score" title="46 reputation points">46</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XQW1123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '15, 09:42</strong> </span></p></div></div><div id="comments-container-42651" class="comments-container"><span id="44942"></span><div id="comment-44942" class="comment"><div id="post-44942-score" class="comment-score"></div><div class="comment-text"><p>hi XQW1123,</p><p>i have the same issue, the xml dissector is displaying the xml file as it is, not in the format i need it to be display.</p><p>i think it should use dtds for that purpose but still i am not able to resolve the issue, please tell me if you got your desired output.</p><p>thanks</p></div><div id="comment-44942-info" class="comment-info"><span class="comment-age">(10 Aug '15, 04:18)</span> <span class="comment-user userinfo">zombimind</span></div></div></div><div id="comment-tools-42651" class="comment-tools"></div><div class="clear"></div><div id="comment-42651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42657"></span>

<div id="answer-container-42657" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42657-score" class="post-score" title="current number of votes">1</div><span id="post-42657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could send the data to the xml dissector, at leas it would be pretty printed in the GUI.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '15, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-42657" class="comments-container"><span id="42675"></span><div id="comment-42675" class="comment"><div id="post-42675-score" class="comment-score"></div><div class="comment-text"><p>Thanks, but do you know if its possible further format the GUI?</p></div><div id="comment-42675-info" class="comment-info"><span class="comment-age">(26 May '15, 13:57)</span> <span class="comment-user userinfo">XQW1123</span></div></div></div><div id="comment-tools-42657" class="comment-tools"></div><div class="clear"></div><div id="comment-42657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

