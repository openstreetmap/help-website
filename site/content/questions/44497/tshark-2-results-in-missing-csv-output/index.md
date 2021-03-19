+++
type = "question"
title = "tshark -2 results in missing CSV output"
description = '''Hi, I have a short SQL/TDS trace and I want to output certain columns into CSV. If I run this command: tshark -T fields -E separator=, -E quote=d -e frame.number -e ip.addr -e _ws.col.Info -r tds_sql_batch_first_10.pcapng  I get: &quot;1&quot;,&quot;10.100.20.223,10.100.20.220&quot;,&quot;1155â┼&#x27;1433 [ACK] Seq=3698378077 Ac...'''
date = "2015-07-26T08:46:00Z"
lastmod = "2015-07-27T06:12:00Z"
weight = 44497
keywords = [ "lua" ]
aliases = [ "/questions/44497" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -2 results in missing CSV output](/questions/44497/tshark-2-results-in-missing-csv-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44497-score" class="post-score" title="current number of votes">0</div><span id="post-44497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a short SQL/TDS trace and I want to output certain columns into CSV. If I run this command:</p><pre><code>tshark -T fields -E separator=, -E quote=d -e frame.number -e ip.addr -e _ws.col.Info -r tds_sql_batch_first_10.pcapng</code></pre><p>I get:</p><pre><code>&quot;1&quot;,&quot;10.100.20.223,10.100.20.220&quot;,&quot;1155â┼&#39;1433 [ACK] Seq=3698378077 Ack=2551614322 Win=65535 Len=0&quot;
&quot;2&quot;,&quot;10.100.20.223,10.100.20.220&quot;,&quot;1154â┼&#39;1433 [ACK] Seq=3762048005 Ack=3002787638 Win=65113 Len=0&quot;
&quot;3&quot;,&quot;10.100.20.223,10.100.20.220&quot;,&quot;SQL batch&quot;
&quot;4&quot;,&quot;10.100.20.220,10.100.20.223&quot;,&quot;Response&quot;
&quot;5&quot;,&quot;10.100.20.223,10.100.20.220&quot;,&quot;1155â┼&#39;1433 [ACK] Seq=3698378553 Ack=2551614538 Win=65319 Len=0&quot;
&quot;6&quot;,&quot;10.100.20.223,10.100.20.220&quot;,&quot;SQL batch&quot;
&quot;7&quot;,&quot;10.100.20.220,10.100.20.223&quot;,&quot;Response&quot;
&quot;8&quot;,&quot;10.100.20.223,10.100.20.220&quot;,&quot;SQL batch&quot;
&quot;9&quot;,&quot;10.100.20.220,10.100.20.223&quot;,&quot;Response&quot;
&quot;10&quot;,&quot;10.100.20.223,10.100.20.220&quot;,&quot;1155â┼&#39;1433 [ACK] Seq=3698379237 Ack=2551614965 Win=64892 Len=0&quot;</code></pre><p>However, I need to run tshark with the -2 (scan twice) option for a LUA I want to use. As a test I run the same command above with the -2 option:</p><pre><code>tshark -2 -T fields -E separator=, -E quote=d -e frame.number -e ip.addr -e _ws.col.Info -r tds_sql_batch_first_10.pcapng</code></pre><p>and this gives this output:</p><pre><code>&quot;1&quot;,&quot;10.100.20.223,10.100.20.220&quot;,
&quot;2&quot;,&quot;10.100.20.223,10.100.20.220&quot;,
&quot;3&quot;,&quot;10.100.20.223,10.100.20.220&quot;,
&quot;4&quot;,&quot;10.100.20.220,10.100.20.223&quot;,
&quot;5&quot;,&quot;10.100.20.223,10.100.20.220&quot;,
&quot;6&quot;,&quot;10.100.20.223,10.100.20.220&quot;,
&quot;7&quot;,&quot;10.100.20.220,10.100.20.223&quot;,
&quot;8&quot;,&quot;10.100.20.223,10.100.20.220&quot;,
&quot;9&quot;,&quot;10.100.20.220,10.100.20.223&quot;,
&quot;10&quot;,&quot;10.100.20.223,10.100.20.220&quot;,</code></pre><p>So the Info column information is missing. I get a similar problem when I add a column from a field defined by my script. Is this what I should expect?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '15, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jul '15, 10:30</strong> </span></p></div></div><div id="comments-container-44497" class="comments-container"></div><div id="comment-tools-44497" class="comment-tools"></div><div class="clear"></div><div id="comment-44497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44498"></span>

<div id="answer-container-44498" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44498-score" class="post-score" title="current number of votes">2</div><span id="post-44498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's a bug. Please submit a bug at <a href="https://bugs.wireshark.org/bugzilla/">bugs.wireshark.org</a>, with the above info. We don't need the capture file or Lua script, because it's a simple bug I can reproduce (and I already know how to fix).</p><p>Also, the weird text output of the info column in the single-pass case is probably due to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11344">Bug 11344</a>, which has been fixed but won't be in a general release version until 1.12.7 is released. (though you can get it now from the <a href="https://www.wireshark.org/download/automated/">automated builds site</a>) If it's not fixed in the automated builds, then it's yet another bug. :)</p><p>Lastly, if what you're trying to do is use Lua to put some info into the CSV output, you don't need to use the INFO column for that - your Lua script can create a new <code>ProtoField</code> which should be reference-able as a field in your tshark command like other fields. (though I've never tried that)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '15, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44498" class="comments-container"><span id="44499"></span><div id="comment-44499" class="comment"><div id="post-44499-score" class="comment-score"></div><div class="comment-text"><p>Thanks Hadriel,</p><p>I do use ProtoField for almost all LUA script output but I have a particular requirement to modify the Info field in Wireshark and I don't want to have to produce one script for Wireshark and another for tshark.</p><p>I'll report the bug.</p><p>Best regards...Paul</p></div><div id="comment-44499-info" class="comment-info"><span class="comment-age">(26 Jul '15, 09:41)</span> <span class="comment-user userinfo">PaulOfford</span></div></div><span id="44501"></span><div id="comment-44501" class="comment"><div id="post-44501-score" class="comment-score"></div><div class="comment-text"><p>Created Bug 11401 - <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11401">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11401</a></p></div><div id="comment-44501-info" class="comment-info"><span class="comment-age">(26 Jul '15, 10:27)</span> <span class="comment-user userinfo">PaulOfford</span></div></div><span id="44517"></span><div id="comment-44517" class="comment"><div id="post-44517-score" class="comment-score"></div><div class="comment-text"><p>Hi Hadriel, Thanks for the rapid work on this. I installed the latest automated build (Wireshark-win64-1.12.7rc0-52-g9d3eb4b.exe) and it works fine.</p></div><div id="comment-44517-info" class="comment-info"><span class="comment-age">(27 Jul '15, 02:54)</span> <span class="comment-user userinfo">PaulOfford</span></div></div><span id="44524"></span><div id="comment-44524" class="comment"><div id="post-44524-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-44524-info" class="comment-info"><span class="comment-age">(27 Jul '15, 06:12)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-44498" class="comment-tools"></div><div class="clear"></div><div id="comment-44498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

