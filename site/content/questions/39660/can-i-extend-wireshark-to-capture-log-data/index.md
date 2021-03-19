+++
type = "question"
title = "Can I extend wireshark to capture log data?"
description = '''I&#x27;m new to Wireshark, so forgive me if the question is dumb. If I have a log data (say from Apache). Can I feed it to Wireshark so I can analyze it? If it requires writing a plugin, I can do that.'''
date = "2015-02-05T03:41:00Z"
lastmod = "2015-02-06T01:35:00Z"
weight = 39660
keywords = [ "data", "log", "format" ]
aliases = [ "/questions/39660" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I extend wireshark to capture log data?](/questions/39660/can-i-extend-wireshark-to-capture-log-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39660-score" class="post-score" title="current number of votes">0</div><span id="post-39660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to Wireshark, so forgive me if the question is dumb.</p><p>If I have a log data (say from Apache). Can I feed it to Wireshark so I can analyze it? If it requires writing a plugin, I can do that.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-log" rel="tag" title="see questions tagged &#39;log&#39;">log</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '15, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/bde9493348770b4f6bf0f632ef91fc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ittay&#39;s gravatar image" /><p><span>Ittay</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ittay has no accepted answers">0%</span></p></div></div><div id="comments-container-39660" class="comments-container"></div><div id="comment-tools-39660" class="comment-tools"></div><div class="clear"></div><div id="comment-39660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39674"></span>

<div id="answer-container-39674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39674-score" class="post-score" title="current number of votes">0</div><span id="post-39674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you write the plugin to do so, then sure.</p><p>If you want to write the plugin in C-code, you might want to look at the code in <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=wiretap/logcat_text.c"><code>logcat_text.c</code></a> to get an idea of how to do it. If you want to write it in Lua, you might want to look at the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=test/lua/acme_file.lua"><code>acme_file.lua</code></a> script.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '15, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39674" class="comments-container"></div><div id="comment-tools-39674" class="comment-tools"></div><div class="clear"></div><div id="comment-39674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39679"></span>

<div id="answer-container-39679" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39679-score" class="post-score" title="current number of votes">0</div><span id="post-39679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While wireshark is awsome and super powerful, it's probably not right tool for the job with logs.</p><p>I'd recommend using ELK stack [elasticsearch, logstash and kibana ] for processing logs</p><p><a href="http://www.elasticsearch.org/">http://www.elasticsearch.org/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '15, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-39679" class="comments-container"></div><div id="comment-tools-39679" class="comment-tools"></div><div class="clear"></div><div id="comment-39679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

