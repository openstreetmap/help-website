+++
type = "question"
title = "Transforming a .pcap file to a CSV file on windows 7 using tshark"
description = '''I&#x27;m having 184MB size PCAP file in this location C:&#92;Program Files&#92;Wireshark&#92;pcap3.pcap I wanted to convert my pcap file into CSV file with some requirement field to analyze network traffic data. Firstly I change my CMD path to &quot;C:&#92;Program Files&#92;Wireshark&quot; to run my tshark command. After that, I chec...'''
date = "2014-11-17T11:28:00Z"
lastmod = "2014-11-17T23:37:00Z"
weight = 37909
keywords = [ "tshark" ]
aliases = [ "/questions/37909" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Transforming a .pcap file to a CSV file on windows 7 using tshark](/questions/37909/transforming-a-pcap-file-to-a-csv-file-on-windows-7-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37909-score" class="post-score" title="current number of votes">0</div><span id="post-37909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having 184MB size PCAP file in this location C:\Program Files\Wireshark\pcap3.pcap</p><p>I wanted to convert my pcap file into CSV file with some requirement field to analyze network traffic data. Firstly I change my CMD path to "<strong>C:\Program Files\Wireshark</strong>" to run my tshark command. After that, I checked my files in that wireshark folder by typing this command "<strong>dir pcap3.pcap</strong>". Then I run this command to break certain column which I wanted " <strong>tshark -r testfile.pcap -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -E header=y -E separator=, -E quote=d -E occurrence=f</strong> ". This command take about 30 minute to complete. Finally i wanted to convert this pcap file into CSV i used this command " <strong>tshark -r testfile.pcap -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -E header=y -E separator=, -E quote=d -E occurrence=f &gt; pcap3.csv</strong> ". When I run the last command it show access denied. Can i know how to solve this things.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/5ef1c8aa6d8084f76534e0f9fdcae545?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Winash&#39;s gravatar image" /><p><span>Winash</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Winash has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> wikified <strong>17 Nov '14, 11:30</strong> </span></p></div></div><div id="comments-container-37909" class="comments-container"></div><div id="comment-tools-37909" class="comment-tools"></div><div class="clear"></div><div id="comment-37909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37910"></span>

<div id="answer-container-37910" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37910-score" class="post-score" title="current number of votes">0</div><span id="post-37910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It would appear that you don't have permission to write to the <code>C:\Program Files\Wireshark\</code> directory. And it's probably not the best location for writing user files anyway. Try specifying an alternate destination, e.g., <code>tshark -r testfile.pcap -T fields ... &gt; C:\Users\Winash\Documents\pcap3.csv</code>.</p><p>You might also want to try adding <code>C:\Program Files\Wireshark\</code> to your <code>PATH</code> environment variable to make it easier to run <code>tshark</code> without having to either specify the full path each time you run it or to change to the <code>C:\Program Files\Wireshark\</code> directory as you seem to be doing now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-37910" class="comments-container"><span id="37914"></span><div id="comment-37914" class="comment"><div id="post-37914-score" class="comment-score"></div><div class="comment-text"><p>An alternative to adding the Wireshark directory to PATH, is to use PowerShell and add an alias, e.g.</p><p><code>New-Alias ts 'C:\Program Files\Wireshark\tshark.exe'</code></p><p>and then use <code>ts</code> as the command.</p></div><div id="comment-37914-info" class="comment-info"><span class="comment-age">(17 Nov '14, 13:35)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37930"></span><div id="comment-37930" class="comment"><div id="post-37930-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I have done with the conversion of data. It's really worked</p></div><div id="comment-37930-info" class="comment-info"><span class="comment-age">(17 Nov '14, 21:27)</span> <span class="comment-user userinfo">Winash</span></div></div><span id="37937"></span><div id="comment-37937" class="comment"><div id="post-37937-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-37937-info" class="comment-info"><span class="comment-age">(17 Nov '14, 23:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37910" class="comment-tools"></div><div class="clear"></div><div id="comment-37910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

