+++
type = "question"
title = "Can Field.new retrieve a field defined previously with ProtoInfo?"
description = '''For example, if you have the postdissector example, and append the following: do  local f_newfield1 = Field.new(&quot;http.newfield1&quot;) end  It fails to start up with the following error: tshark: Lua: Error during loading:  [string &quot;/home/alastair/.wireshark/plugins/http_extr...&quot;]:38: bad argument #1 to &#x27;...'''
date = "2014-03-04T08:51:00Z"
lastmod = "2014-03-04T12:05:00Z"
weight = 30403
keywords = [ "lua", "postdissector", "field" ]
aliases = [ "/questions/30403" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can Field.new retrieve a field defined previously with ProtoInfo?](/questions/30403/can-fieldnew-retrieve-a-field-defined-previously-with-protoinfo)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30403-score" class="post-score" title="current number of votes">0</div><span id="post-30403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For example, if you have the <a href="http://wiki.wireshark.org/Lua/Dissectors">postdissector example</a>, and append the following:</p><pre><code>do
    local f_newfield1 = Field.new(&quot;http.newfield1&quot;)
end</code></pre><p>It fails to start up with the following error:</p><pre><code>tshark: Lua: Error during loading:
 [string &quot;/home/alastair/.wireshark/plugins/http_extr...&quot;]:38: bad argument #1 to &#39;new&#39; (Field_new: a field with this name must exist)</code></pre><p>.. even though the field was defined previously as a ProtoField.</p><p>Is this a bug or feature or something else?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span> <span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '14, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/b505e6c822ccf1eaa8d663d9fb28fedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randomphrase&#39;s gravatar image" /><p><span>randomphrase</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randomphrase has no accepted answers">0%</span></p></div></div><div id="comments-container-30403" class="comments-container"></div><div id="comment-tools-30403" class="comment-tools"></div><div class="clear"></div><div id="comment-30403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30406"></span>

<div id="answer-container-30406" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30406-score" class="post-score" title="current number of votes">0</div><span id="post-30406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="randomphrase has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What version are you running?</p><p>The ability to use a Field extractor (i.e., to call Field.new()) of a field created by your script was only possible relatively recently - as a fix in bug 3513, back in October. I think that means you have to be running Wireshark version 1.11 at least. (I think 1.10 was cut before then, so it won't have this because the bug wasn't critical) I could be wrong though - it might have gotten backported into 1.10 at some point.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '14, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30406" class="comments-container"><span id="30407"></span><div id="comment-30407" class="comment"><div id="post-30407-score" class="comment-score"></div><div class="comment-text"><p>Just checked - no it's not in 1.10, you need to go to 1.11.2, which you can get on the downloads page.</p></div><div id="comment-30407-info" class="comment-info"><span class="comment-age">(04 Mar '14, 09:33)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30416"></span><div id="comment-30416" class="comment"><div id="post-30416-score" class="comment-score"></div><div class="comment-text"><p>Yep that was the problem - Thanks for the timely answer!</p></div><div id="comment-30416-info" class="comment-info"><span class="comment-age">(04 Mar '14, 12:05)</span> <span class="comment-user userinfo">randomphrase</span></div></div></div><div id="comment-tools-30406" class="comment-tools"></div><div class="clear"></div><div id="comment-30406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

