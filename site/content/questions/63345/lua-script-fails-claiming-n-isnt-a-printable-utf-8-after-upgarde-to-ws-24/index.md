+++
type = "question"
title = "LUA: Script fails claiming &#92;n isn&#x27;t a printable UTF-8 after upgarde to WS 2.4"
description = '''Hi, I have a LUA script that throws the following error: **(tshark.exe:16500): ERROR**: Title for preference tsumcli.header isn&#x27;t printable UTF-8.  The script line that tshark is complaining about is: tsumcli.prefs.header = Pref.statictext(&quot;TRANSUM r14&#92;n&#92;n&quot;, &quot;See the online manual for full details.&quot;...'''
date = "2017-08-02T10:15:00Z"
lastmod = "2017-08-02T11:30:00Z"
weight = 63345
keywords = [ "lua", "errors", "tshark" ]
aliases = [ "/questions/63345" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [LUA: Script fails claiming \\n isn't a printable UTF-8 after upgarde to WS 2.4](/questions/63345/lua-script-fails-claiming-n-isnt-a-printable-utf-8-after-upgarde-to-ws-24)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63345-score" class="post-score" title="current number of votes">0</div><span id="post-63345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a LUA script that throws the following error:</p><pre><code>**(tshark.exe:16500): ERROR**: Title for preference tsumcli.header isn&#39;t printable UTF-8.</code></pre><p>The script line that tshark is complaining about is:</p><pre><code>tsumcli.prefs.header = Pref.statictext(&quot;TRANSUM r14\n\n&quot;, &quot;See the online manual for full details.&quot;)</code></pre><p>If I remove the two new line characters I don't get the problem. Interestingly, I don't get the problem with the following line either:</p><pre><code>tsumcli.prefs.tcpports = Pref.range(&quot;Output RTE data for these TCP service ports&quot;, &quot;25,80,443,1433&quot;, &quot;Add and remove ports numbers separated by commas\nRanges are not supported&quot;, 65535)</code></pre><p>Is \n illegal or is this a bug?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '17, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-63345" class="comments-container"></div><div id="comment-tools-63345" class="comment-tools"></div><div class="clear"></div><div id="comment-63345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63348"></span>

<div id="answer-container-63348" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63348-score" class="post-score" title="current number of votes">1</div><span id="post-63348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PaulOfford has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>\n <em>isn't</em> a printable UTF-8 character; control characters aren't printable characters. Newlines, tabs, etc. do <em>not</em> belong in preference titles.</p><blockquote><p>If I remove the two new line characters I don't get the problem.</p></blockquote><p>That is the right thing to do - remove the non-printable characters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '17, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-63348" class="comments-container"><span id="63349"></span><div id="comment-63349" class="comment"><div id="post-63349-score" class="comment-score"></div><div class="comment-text"><p>Specifically, it was <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=cbf89c8ed842a58c282872cf8c42adf9b8b2ffee">this</a> commit from Gerald that made all non-printable characters illegal, so no it's not a bug but intentional.</p></div><div id="comment-63349-info" class="comment-info"><span class="comment-age">(02 Aug '17, 11:30)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-63348" class="comment-tools"></div><div class="clear"></div><div id="comment-63348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

