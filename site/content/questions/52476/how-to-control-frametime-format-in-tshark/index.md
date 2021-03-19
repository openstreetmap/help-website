+++
type = "question"
title = "How to control frame.time format in tshark?"
description = '''Hi, I have a pcap file and I have converted it to a csv file by tshark command and load it into a table in MySQL database.  tshark -r normal1.pcap -T fields -e frame.number -e frame.time -e frame.len -e ip.version -e ip.hdr_len -e ip.len -e ip.flags -e ip.dst -e ip.src -e ip.proto -e _ws.col.Protoco...'''
date = "2016-05-12T11:10:00Z"
lastmod = "2016-05-19T14:44:00Z"
weight = 52476
keywords = [ "frame.time", "tshark" ]
aliases = [ "/questions/52476" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to control frame.time format in tshark?](/questions/52476/how-to-control-frametime-format-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52476-score" class="post-score" title="current number of votes">0</div><span id="post-52476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a pcap file and I have converted it to a csv file by tshark command and load it into a table in MySQL database.</p><blockquote><p>tshark -r normal1.pcap -T fields -e frame.number -e frame.time -e frame.len -e ip.version -e ip.hdr_len -e ip.len -e ip.flags -e ip.dst -e ip.src -e ip.proto -e _ws.col.Protocol -e ip.ttl -e tcp.dstport -E header=y -E separator=, -E quote=d -E occurrence=f &gt; D:\distancce\captures\normal\normal1.csv</p></blockquote><p>Everything works okay, but I have a problem in frame.time field It does not appear in the database and instead appear zeros, Although in the csv file does not exist zeros there is a time format like this</p><blockquote><p>"May 12, 2016 10:49:12.648156000 Paris, Madrid (heure d'été)"</p></blockquote><p>how I can get a time format in the data base like time format in csv file.</p><p>thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame.time" rel="tag" title="see questions tagged &#39;frame.time&#39;">frame.time</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '16, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/279908d3c8338ae7ec02baa9f51a3c1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Khadidja%20Khadidja&#39;s gravatar image" /><p><span>Khadidja Kha...</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Khadidja Khadidja has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 May '16, 13:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-52476" class="comments-container"></div><div id="comment-tools-52476" class="comment-tools"></div><div class="clear"></div><div id="comment-52476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52480"></span>

<div id="answer-container-52480" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52480-score" class="post-score" title="current number of votes">1</div><span id="post-52480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Edit:</p><p>withdrawing what I've posted as an Answer, as the correct Answer can be found <a href="https://ask.wireshark.org/questions/30393/tshark-how-to-output-date-in-iso-format">here</a>.</p><p><del>Put this way it is almost a "not a Wireshark question", and worse than that, it is even not a question which could be answered completely, because it lacks information about the date&amp;time format used by the database.</del></p><del></del><p>As things stand right now, you cannot influence what format tshark will use to print the <code>frame.time</code> value, as the <code>-t</code> option only changes the format used to display the value of this field in packet summary headers. This is maybe worth filing a bug with severity level "enhancement".</p><p>So for the time being, you'll need to use some post-process of the output of tshark to convert the timestamp format output by tshark to a format the database understands.</p></s><p><del>NB: even if the enhancement mentioned above would be implemented, the current implementation of the <code>-t</code> option is a choice from several pre-defined formats. So if none of them matches the expectations of the database, which is quite likely to be true, you'd still need a post-process.</del></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '16, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '16, 10:58</strong> </span></p></div></div><div id="comments-container-52480" class="comments-container"><span id="52792"></span><div id="comment-52792" class="comment"><div id="post-52792-score" class="comment-score"></div><div class="comment-text"><p>thanks :).</p></div><div id="comment-52792-info" class="comment-info"><span class="comment-age">(19 May '16, 14:44)</span> <span class="comment-user userinfo">Khadidja Kha...</span></div></div></div><div id="comment-tools-52480" class="comment-tools"></div><div class="clear"></div><div id="comment-52480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

