+++
type = "question"
title = "limit search to within one particular packet"
description = '''Hi, I know how to use a filter to find particular packets. But what if I just want to find something within a particular packet? For example, I have a packet with lots of measurements. Each measurement is a tree item. I want to see if one particular measurement (say id &quot;mea20004&quot;) occurs more than o...'''
date = "2014-04-22T09:59:00Z"
lastmod = "2014-04-24T15:45:00Z"
weight = 32064
keywords = [ "limited", "search", "one", "packet", "to" ]
aliases = [ "/questions/32064" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [limit search to within one particular packet](/questions/32064/limit-search-to-within-one-particular-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32064-score" class="post-score" title="current number of votes">0</div><span id="post-32064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I know how to use a filter to find particular packets.</p><p>But what if I just want to find something within a particular packet?</p><p>For example, I have a packet with lots of measurements. Each measurement is a tree item. I want to see if one particular measurement (say id "mea20004") occurs more than once. I can painstakingly visually going through the entire tree and find all the items with that id, or is there a way I can use keyboard combo or filter to search for it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-limited" rel="tag" title="see questions tagged &#39;limited&#39;">limited</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-one" rel="tag" title="see questions tagged &#39;one&#39;">one</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '14, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p><span>YXI</span><br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div></div><div id="comments-container-32064" class="comments-container"><span id="32108"></span><div id="comment-32108" class="comment"><div id="post-32108-score" class="comment-score"></div><div class="comment-text"><p>I saw a way to do this in Wireshark, but it's not working all correctly. In Edit-&gt;Find Packet, you can choose By String, and Search in Packet details.<br />
Good news is it finds the first occurrence of my measurement. However, then no matter what you do, either find next, find previous, direction up, or down, it keeps locating the first occurrence, not the next ones.<br />
Is this a bug?</p></div><div id="comment-32108-info" class="comment-info"><span class="comment-age">(23 Apr '14, 08:24)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="32109"></span><div id="comment-32109" class="comment"><div id="post-32109-score" class="comment-score"></div><div class="comment-text"><p>OK, find next will find the string in the next packet, not the second time the string occurs in the same packet. That's not what I need then.</p></div><div id="comment-32109-info" class="comment-info"><span class="comment-age">(23 Apr '14, 08:51)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="32112"></span><div id="comment-32112" class="comment"><div id="post-32112-score" class="comment-score"></div><div class="comment-text"><p>what is your protocol and is this you own (custom) dissector?</p></div><div id="comment-32112-info" class="comment-info"><span class="comment-age">(23 Apr '14, 11:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32147"></span><div id="comment-32147" class="comment"><div id="post-32147-score" class="comment-score"></div><div class="comment-text"><p>Yes, it is my own dissector in Lua.</p></div><div id="comment-32147-info" class="comment-info"><span class="comment-age">(24 Apr '14, 07:15)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-32064" class="comment-tools"></div><div class="clear"></div><div id="comment-32064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32068"></span>

<div id="answer-container-32068" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32068-score" class="post-score" title="current number of votes">0</div><span id="post-32068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="YXI has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Command line, GNU grep, and tshark e.g.</p><blockquote><p>tshark -r file.pcap -R "frame.number == X" | grep -wc mea20004</p></blockquote><p>where X is the frame number. This should work on all UN*Xes that have a <code>grep</code> command that supports <code>-w</code> and <code>-c</code>, such as GNU grep, and may work on Windows if you have a version of <code>grep</code> like that available.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '14, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Apr '14, 15:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-32068" class="comments-container"><span id="32105"></span><div id="comment-32105" class="comment"><div id="post-32105-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks so much.<br />
I modified the command. The main thing is the -V option. Have to have that.</p><p>tshark -r myCaputre.pcap -Y "frame.number==49" -V |grep -n mea20004</p><p>142: Values for MeasurementID: mea20004</p><p>175: Values for MeasurementID: mea20004</p><p>This is helpful, but I really want a solution using Wireshark instead of tshark. The reason is I would like to see where the two occurrences are in the full tree. Just knowing line numbers is not very intuitive.</p><p>Is there a way to do this inside Wireshark?</p></div><div id="comment-32105-info" class="comment-info"><span class="comment-age">(23 Apr '14, 08:09)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-32068" class="comment-tools"></div><div class="clear"></div><div id="comment-32068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32164"></span>

<div id="answer-container-32164" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32164-score" class="post-score" title="current number of votes">0</div><span id="post-32164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>or is there a way I can use keyboard combo or filter to search for it?</p></blockquote><p>No.</p><p>The ability to search within a packet, separate from the ability to search within the list of packets, would probably be a useful new feature. You should probably file this as an enhancement request on <a href="http://bugs.wireshark.org/">the Wireshark bugzilla</a>; the Q&amp;A site is probably not the best place to discuss the details of a requested new feature.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '14, 15:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-32164" class="comments-container"></div><div id="comment-tools-32164" class="comment-tools"></div><div class="clear"></div><div id="comment-32164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

