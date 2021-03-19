+++
type = "question"
title = "Using the wireshark pcap file capture data as Splunk Log Data"
description = '''Can i use the wireshark pcap file capture data and store the data into Splunk for indexing?'''
date = "2012-04-15T18:51:00Z"
lastmod = "2012-04-16T10:13:00Z"
weight = 10165
keywords = [ "capture", "pcap", "splunk" ]
aliases = [ "/questions/10165" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using the wireshark pcap file capture data as Splunk Log Data](/questions/10165/using-the-wireshark-pcap-file-capture-data-as-splunk-log-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10165-score" class="post-score" title="current number of votes">0</div><span id="post-10165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can i use the wireshark pcap file capture data and store the data into Splunk for indexing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-splunk" rel="tag" title="see questions tagged &#39;splunk&#39;">splunk</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '12, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p><span>misteryuku</span><br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Apr '12, 18:51</strong> </span></p></div></div><div id="comments-container-10165" class="comments-container"></div><div id="comment-tools-10165" class="comment-tools"></div><div class="clear"></div><div id="comment-10165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10170"></span>

<div id="answer-container-10170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10170-score" class="post-score" title="current number of votes">0</div><span id="post-10170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Probably. Using either Wireshark, or more likely tshark and setting options to output only the fields required and using a csv format the data could be fed into Splunk.</p><p>If you can explain exactly what data you wish to extract from the pcap files someone should be able to give you a recipe for doing that.</p><p>Actually getting the data into Splunk is not a suitable topic for this site though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '12, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10170" class="comments-container"></div><div id="comment-tools-10170" class="comment-tools"></div><div class="clear"></div><div id="comment-10170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10171"></span>

<div id="answer-container-10171" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10171-score" class="post-score" title="current number of votes">0</div><span id="post-10171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, if you check on <a href="http://splunk-base.splunk.com/answers/">the Splunk Q&amp;A site</a>, that question <a href="http://splunk-base.splunk.com/answers/2922/splunk-monitoring-a-wireshark-file">appears to have been answered already</a>, and the answer, sadly, is "no", as Splunk appears, at least from what one answer to that question says, to read only text files, and pcap files are <em>NOT</em> text files. Other answers seem to indicate that if you feed a pcap file to TShark and have it print out the file in verbose format, Splunk can read the resulting text file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '12, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10171" class="comments-container"><span id="10174"></span><div id="comment-10174" class="comment"><div id="post-10174-score" class="comment-score"></div><div class="comment-text"><p>So the way is to convert the pcap to a csv file using tshark commands is that right???</p></div><div id="comment-10174-info" class="comment-info"><span class="comment-age">(16 Apr '12, 01:25)</span> <span class="comment-user userinfo">misteryuku</span></div></div><span id="10192"></span><div id="comment-10192" class="comment"><div id="post-10192-score" class="comment-score"></div><div class="comment-text"><p>In the answer on the Splunk Q&amp;A site, they converted it to a human-readable display of the full protocol tree, not a CSV file. If you want further help in getting Splunk to process a pcap file, the best place to ask is on the Spunk Q&amp;A site, as those people are more likely to know what Splunk would most usefully process.</p></div><div id="comment-10192-info" class="comment-info"><span class="comment-age">(16 Apr '12, 10:13)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-10171" class="comment-tools"></div><div class="clear"></div><div id="comment-10171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

