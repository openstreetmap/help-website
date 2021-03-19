+++
type = "question"
title = "Dissector: ignore &quot;0x00&quot; in a string (FT_STRING)?"
description = '''Hi, I am writing a custom Wireshark dissector which needs to show some strings. Let me say there is some hex code like &quot;48 65 6c 6c 6f&quot; which is &quot;Hello&quot;. This is interpreted fine by using FT_STRING in the hf_ declaration. If this hex codes contain something like &quot;48 65 6c 6c 6f 00 48 65 6c 6c 6f&quot;, t...'''
date = "2013-10-01T01:45:00Z"
lastmod = "2013-10-01T01:45:00Z"
weight = 25441
keywords = [ "ft_string", "dissector", "string", "wireshark" ]
aliases = [ "/questions/25441" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector: ignore "0x00" in a string (FT\_STRING)?](/questions/25441/dissector-ignore-0x00-in-a-string-ft_string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25441-score" class="post-score" title="current number of votes">0</div><span id="post-25441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am writing a custom Wireshark dissector which needs to show some strings. Let me say there is some hex code like "48 65 6c 6c 6f" which is "Hello". This is interpreted fine by using FT_STRING in the hf_ declaration. If this hex codes contain something like "48 65 6c 6c 6f 00 48 65 6c 6c 6f", the second "Hello" gets not displayed in the UI. I assume it is because of the "00" in between. Is there a way to convince Wireshark not to interpret "00" as a string termination but continue displaying the string?</p><p>Thanks, hhhannes</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ft_string" rel="tag" title="see questions tagged &#39;ft_string&#39;">ft_string</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-string" rel="tag" title="see questions tagged &#39;string&#39;">string</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '13, 01:45</strong></p><img src="https://secure.gravatar.com/avatar/d2ad1b223f1bf47ca43b6c37865b7257?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hhhannes&#39;s gravatar image" /><p><span>hhhannes</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hhhannes has no accepted answers">0%</span></p></div></div><div id="comments-container-25441" class="comments-container"></div><div id="comment-tools-25441" class="comment-tools"></div><div class="clear"></div><div id="comment-25441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

