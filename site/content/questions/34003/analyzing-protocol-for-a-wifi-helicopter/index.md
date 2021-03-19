+++
type = "question"
title = "analyzing protocol for a WiFi helicopter"
description = '''I&#x27;m working on reverse engineering the protocol that&#x27;s going between an iPhone app and a WiFi controlled helicopter. It&#x27;s being complicated because the app sends 18 bytes of data every .04 seconds even if the control values do not change. I already have a filter that selects only the packets with th...'''
date = "2014-06-20T16:57:00Z"
lastmod = "2014-06-21T16:49:00Z"
weight = 34003
keywords = [ "data", "export", "missing" ]
aliases = [ "/questions/34003" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [analyzing protocol for a WiFi helicopter](/questions/34003/analyzing-protocol-for-a-wifi-helicopter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34003-score" class="post-score" title="current number of votes">0</div><span id="post-34003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on reverse engineering the protocol that's going between an iPhone app and a WiFi controlled helicopter.</p><p>It's being complicated because the app sends 18 bytes of data every .04 seconds even if the control values do not change.</p><p>I already have a filter that selects only the packets with these messages. I have two problems</p><ol><li>I get entries for packets where data was missed, I assume they were not captured. This clutters up the capture and makes it hard to read. What can I add to the filter to make it ignore the missed data and just show the successful captures?</li><li>Is there any way I can export just the stream of 18 byte messages to look at with an external program?</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '14, 16:57</strong></p><img src="https://secure.gravatar.com/avatar/3b4ac9ee0a0db93cb1a7b4cb7e960a35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MiloMindbender&#39;s gravatar image" /><p><span>MiloMindbender</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MiloMindbender has no accepted answers">0%</span></p></div></div><div id="comments-container-34003" class="comments-container"><span id="34007"></span><div id="comment-34007" class="comment"><div id="post-34007-score" class="comment-score"></div><div class="comment-text"><p>Cool project! If it's TCP, click Edit -&gt; Preferences, expand the Protocols list, find TCP, and unselect "Analyze TCP Sequence Numbers". To save just the data, right-click on any packet and select "Follow TCP Stream". In the dialog box, change the "Entire Conversation" drop-down box and select the strea (helicopter)-&gt;(wireshark). Select the ASCII radio button if you'd like, then click the Save button.</p></div><div id="comment-34007-info" class="comment-info"><span class="comment-age">(20 Jun '14, 17:40)</span> <span class="comment-user userinfo">smp</span></div></div></div><div id="comment-tools-34003" class="comment-tools"></div><div class="clear"></div><div id="comment-34003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34021"></span>

<div id="answer-container-34021" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34021-score" class="post-score" title="current number of votes">0</div><span id="post-34021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Regarding #1:</p><blockquote><p>What can I add to the filter to make it ignore the missed data</p></blockquote><p>hard to tell, without an example. Is it possible to post a sample capture file somewhere (google drive, dropbox, cloudshark.org). Please add some information about the frame numbers where you have identified 'missing data'.</p><p>Regarding #2:</p><blockquote><p>Is there any way I can export just the stream of 18 byte messages to look at with an external program?</p></blockquote><p>Again, hard to tell, without knowing the protocol (HTTP ?). In general, you can use <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> on the CLI to print the payload of frames.</p><blockquote><p>tshark -nr input.pcap -T pdml<br />
tshark -nr input.pcap -V</p></blockquote><p>These are only two generic ways to export the bytes. If you are able to post a sample capture file, we might be able to narrow it down to a better/different method.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '14, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-34021" class="comments-container"></div><div id="comment-tools-34021" class="comment-tools"></div><div class="clear"></div><div id="comment-34021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

