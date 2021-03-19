+++
type = "question"
title = "Converting a wireshark pcap file to a windows txt file that contains field=value data."
description = '''What is the tshark command for converting a wireshark pcap file to a windows .txt file that will result in the output in the windows .txt file shown below? (The x&#x27;s represents a numeric value of the ip address.) Sample output :  No=1,Time=0.000000,source=xxx.xxx.xxx.xxx,Destination=xxx.xxx.xxx.xxx,P...'''
date = "2012-04-18T18:13:00Z"
lastmod = "2012-04-19T00:02:00Z"
weight = 10256
keywords = [ "windows", "txt", "pcap", "tshark" ]
aliases = [ "/questions/10256" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Converting a wireshark pcap file to a windows txt file that contains field=value data.](/questions/10256/converting-a-wireshark-pcap-file-to-a-windows-txt-file-that-contains-fieldvalue-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10256-score" class="post-score" title="current number of votes">0</div><span id="post-10256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the tshark command for converting a wireshark pcap file to a windows .txt file that will result in the output in the windows .txt file shown below? (The x's represents a numeric value of the ip address.)</p><p>Sample output : No=1,Time=0.000000,source=xxx.xxx.xxx.xxx,Destination=xxx.xxx.xxx.xxx,Protocol=TCP,Length=54,Info=35165 &gt; http [SYN] Seq=0 Win=16384 Len=0 No=2,Time=0.000001,source=xxx.xxx.xxx.xxx,Destination=xxx.xxx.xxx.xxx,Protocol=TCP,Length=54,Info=14378 &gt; http [SYN] Seq=0 Win=16384 Len=0 No=3,Time=0.000003,source=xxx.xxx.xxx.xxx,Destination=xxx.xxx.xxx.xxx,Protocol=TCP,Length=54,Info=31944 &gt; http [SYN] Seq=0 Win=16384 Len=0</p><p>and so on......util the end of the capture.</p><p>I know that tshark has some syntax like this i have no idea how to put it so that i can generate the above output to a .txt file</p><p>-E&lt;fieldsoption&gt;=&lt;value&gt; set options for output when -Tfields selected: header=y|n switch headers on and off separator=/t|/s|&lt;char&gt; select tab, space, printable character as separator occurrence=f|l|a print first, last or all occurrences of each field aggregator=,|/s|&lt;char&gt; select comma, space, printable character as aggregator</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-txt" rel="tag" title="see questions tagged &#39;txt&#39;">txt</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '12, 18:13</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p><span>misteryuku</span><br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '12, 22:08</strong> </span></p></div></div><div id="comments-container-10256" class="comments-container"></div><div id="comment-tools-10256" class="comment-tools"></div><div class="clear"></div><div id="comment-10256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10261"></span>

<div id="answer-container-10261" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10261-score" class="post-score" title="current number of votes">1</div><span id="post-10261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, you <em>don't</em> know that TShark has some syntax like this, and you <em>can't possibly</em> know it, because TShark <em>doesn't</em> have a syntax like that. There is no TShark command that will do that. Tshark has no option to show key=value output, whether for columns or fields.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '12, 23:58</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10261" class="comments-container"><span id="10262"></span><div id="comment-10262" class="comment"><div id="post-10262-score" class="comment-score"></div><div class="comment-text"><p>Okay i get it.</p></div><div id="comment-10262-info" class="comment-info"><span class="comment-age">(19 Apr '12, 00:02)</span> <span class="comment-user userinfo">misteryuku</span></div></div></div><div id="comment-tools-10261" class="comment-tools"></div><div class="clear"></div><div id="comment-10261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

