+++
type = "question"
title = "Is regex lookaround supported in wireshark display filters?"
description = '''Is it supported?'''
date = "2015-08-26T10:26:00Z"
lastmod = "2015-08-27T09:22:00Z"
weight = 45368
keywords = [ "regex", "display-filter" ]
aliases = [ "/questions/45368" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is regex lookaround supported in wireshark display filters?](/questions/45368/is-regex-lookaround-supported-in-wireshark-display-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45368-score" class="post-score" title="current number of votes">0</div><span id="post-45368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it supported?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-regex" rel="tag" title="see questions tagged &#39;regex&#39;">regex</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '15, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/a5a75ed88e2a780afa7231bbfb7f21bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MrKang&#39;s gravatar image" /><p><span>MrKang</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MrKang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '15, 07:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-45368" class="comments-container"><span id="45378"></span><div id="comment-45378" class="comment"><div id="post-45378-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "regex in wireshark" - what feature in Wireshark in particular are you trying to use a regex with? Display filters? And how are you trying to use a lookaround exactly?</p><p>I ask because yes, Wireshark's internal regex engine supports lookarounds - its internal engine is PCRE. (well... Glib's version of PCRE anyway)</p></div><div id="comment-45378-info" class="comment-info"><span class="comment-age">(26 Aug '15, 17:56)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="45392"></span><div id="comment-45392" class="comment"><div id="post-45392-score" class="comment-score"></div><div class="comment-text"><p>Hi Hadriel. Yes i want to use lookaroud feature of regex in wireshark(v1.12.7). I have used below display filters.</p><p>http.request and http matches "(?m)(?&lt;!\x0d)\x0a$"</p><p>I want to find packet that finished by OA only. But that display filters found packet that finished by 0D0A and 0A.</p></div><div id="comment-45392-info" class="comment-info"><span class="comment-age">(27 Aug '15, 02:58)</span> <span class="comment-user userinfo">MrKang</span></div></div></div><div id="comment-tools-45368" class="comment-tools"></div><div class="clear"></div><div id="comment-45368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45402"></span>

<div id="answer-container-45402" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45402-score" class="post-score" title="current number of votes">1</div><span id="post-45402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It works for me.</p><p>I think the problem is that you're expecting the field "<code>http</code>" to only be the HTTP header portion of the message - i.e., the bytes highlighted when you click on the "HTTP" item in the display tree of the Packet Details window pane. But in fact the "http" field includes the body of the HTTP message as well, so your regex is getting executed against the entire HTTP message basically, and there's likely a "<code>0A</code>" byte, without a "<code>0D</code>" byte before it, inside the body somewhere.</p><p>Also, on a side note: Wireshark uses Glib's implementation of PCRE, which is real PCRE but with certain defaults changed. One of them is what a "newline" is by default, with respect to anchor matching for "<code>^</code>" and "<code>$</code>" in multiline mode. Glib treats either a carriage-return or linefeed or both as newlines by default for such cases (i.e., the same as "<code>\R</code>"), whereas I believe normal PCRE would only consider a linefeed ("<code>\n</code>" or "<code>0A</code>") as a "newline" for those cases. I don't think this would impact your match, but since your regex set multimode and used the "<code>$</code>" anchor, I thought I'd mention the difference.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '15, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-45402" class="comments-container"><span id="45408"></span><div id="comment-45408" class="comment"><div id="post-45408-score" class="comment-score"></div><div class="comment-text"><p>I have understood. I did packet check again. The packet that finished by 0D0A and 0A is body of the HTTP message. Thank you.:)</p></div><div id="comment-45408-info" class="comment-info"><span class="comment-age">(27 Aug '15, 09:22)</span> <span class="comment-user userinfo">MrKang</span></div></div></div><div id="comment-tools-45402" class="comment-tools"></div><div class="clear"></div><div id="comment-45402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

