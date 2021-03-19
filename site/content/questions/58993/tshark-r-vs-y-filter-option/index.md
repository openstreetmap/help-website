+++
type = "question"
title = "Tshark -R vs -Y filter option"
description = '''tshark provides -R and -Y filters, what is the difference between read filter -R and display filter -Y. I have been using the -Y option to apply a filter to get a subset of the logs while converting them to pdml (xml) for further processing. tshark -r source.pcap -Y &quot;(s1ap.procedureCode == 13 &amp;amp;&amp;...'''
date = "2017-01-23T19:07:00Z"
lastmod = "2017-01-24T02:04:00Z"
weight = 58993
keywords = [ "tshark" ]
aliases = [ "/questions/58993" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark -R vs -Y filter option](/questions/58993/tshark-r-vs-y-filter-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58993-score" class="post-score" title="current number of votes">0</div><span id="post-58993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>tshark provides <code>-R</code> and <code>-Y</code> filters, what is the difference between read filter <code>-R</code> and display filter <code>-Y</code>. I have been using the <code>-Y</code> option to apply a filter to get a subset of the logs while converting them to pdml (xml) for further processing.</p><pre><code>tshark -r source.pcap -Y &quot;(s1ap.procedureCode == 13 &amp;&amp; nas_eps.nas_msg_emm_type == 0x5e )&quot; -T pdml &gt; filtered_xml.xml</code></pre><p>This works fine on windows build. However -Y is an invalid option on linux build.</p><pre><code>mymachine{66}$ tshark -v
TShark 1.8.10 (SVN Rev Unknown from unknown)</code></pre><ul><li>what is the difference between the <code>-Y</code> and <code>-R</code> filter options ?</li><li>In the linux build I do not see the <code>-Y</code> option, what is the equivalent that can be used ?</li></ul><p>From <code>tshark -h</code> on windows</p><pre><code>-R &lt;read filter&gt;         packet Read filter in Wireshark display filter syntax

-Y &lt;display filter&gt;      packet displaY filter in Wireshark display filter</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '17, 19:07</strong></p><img src="https://secure.gravatar.com/avatar/d1d9561850217ca49173676d29d4632d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wire990099&#39;s gravatar image" /><p><span>wire990099</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wire990099 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Jan '17, 20:25</strong> </span></p></div></div><div id="comments-container-58993" class="comments-container"></div><div id="comment-tools-58993" class="comment-tools"></div><div class="clear"></div><div id="comment-58993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59004"></span>

<div id="answer-container-59004" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59004-score" class="post-score" title="current number of votes">0</div><span id="post-59004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wire990099 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>-R filters packets during the first pass of analysis.</p><p>-Y filter packets on single-pass dissect.</p><p>"Normally" on a current tshark (2.2.X) you would use -Y. However your tshark version is pretty old (1.8.10). Here you have to use -R.</p><p>-Y has been introduced with 1.10.X</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '17, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-59004" class="comments-container"></div><div id="comment-tools-59004" class="comment-tools"></div><div class="clear"></div><div id="comment-59004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

