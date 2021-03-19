+++
type = "question"
title = "Select Ip source addresses with 100 packets or more and save to another file"
description = '''I have a large pcap file that I split in several smaller files using editcap. I sorted each file by IP source address, (using |sort -k 3 command), but now I need to select only those IP source addresses with 100 packets or more, and then write only those addresses to another file for further filteri...'''
date = "2016-11-23T20:03:00Z"
lastmod = "2016-11-24T22:10:00Z"
weight = 57591
keywords = [ "ip", "100", "packets", "file", "source" ]
aliases = [ "/questions/57591" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Select Ip source addresses with 100 packets or more and save to another file](/questions/57591/select-ip-source-addresses-with-100-packets-or-more-and-save-to-another-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57591-score" class="post-score" title="current number of votes">0</div><span id="post-57591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a large pcap file that I split in several smaller files using editcap. I sorted each file by IP source address, (using |sort -k 3 command), but now I need to select only those IP source addresses with 100 packets or more, and then write only those addresses to another file for further filtering. I need to do that from command line because I have to write a bash script to do that for all smaller files resulting from the split (about 800 files). Help is greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-100" rel="tag" title="see questions tagged &#39;100&#39;">100</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '16, 20:03</strong></p><img src="https://secure.gravatar.com/avatar/b3f6579bb81c4e2875f9293da09b05c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MaryR&#39;s gravatar image" /><p><span>MaryR</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MaryR has no accepted answers">0%</span></p></div></div><div id="comments-container-57591" class="comments-container"><span id="57593"></span><div id="comment-57593" class="comment"><div id="post-57593-score" class="comment-score"></div><div class="comment-text"><p>In what form is your packet data? From the description I assume it's not in PCAP files. Would that be CSV files instead?</p></div><div id="comment-57593-info" class="comment-info"><span class="comment-age">(24 Nov '16, 01:20)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="57607"></span><div id="comment-57607" class="comment"><div id="post-57607-score" class="comment-score"></div><div class="comment-text"><p>I forgot to mention it is a pcap file. Thanks.</p></div><div id="comment-57607-info" class="comment-info"><span class="comment-age">(24 Nov '16, 06:51)</span> <span class="comment-user userinfo">MaryR</span></div></div></div><div id="comment-tools-57591" class="comment-tools"></div><div class="clear"></div><div id="comment-57591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57595"></span>

<div id="answer-container-57595" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57595-score" class="post-score" title="current number of votes">2</div><span id="post-57595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MaryR has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could script something like this to create a list of all IP addresses with at least 100 packets in a single small file:</p><pre><code>for file in `ls -1 &lt;all-small-files&gt;`
do
    tshark -r $file -T fields -e ip.src | sort | uniq -c | awk &#39;$1 &gt;= 100 {print $2}&#39; 
done | sort -u &gt; ip-with-100-packets.txt</code></pre><p>Or you could use tcpdump on the large file (as it does not keep state and therefor can handle the big file without running out of memory). :</p><pre><code>tcpdump -n -r netflix.pcapng  | cut -d &#39; &#39; -f 3 | sed -Ee &#39;s/\.[0-9]+$//&#39; | sort | uniq -c | awk &#39;$1 &gt;= 100 {print $2}&#39; &gt; ip-with-100-packets.txt</code></pre><p>This will give you all ip's with at least 100 packets in the original large file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '16, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-57595" class="comments-container"><span id="57612"></span><div id="comment-57612" class="comment"><div id="post-57612-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much for these solutions SYN-bit. The second solution in my computer is taking 15 min + (still running), so perhaps file is too large (822 MB). But for the first solution, is there a way to still keep the time stamp (2nd field) and the TCP/UDP (5th field) fields, in addition to the IP source address field in the resulting file? Because I still have to verify that each of those 100+packet flows have a duration of at least 60 seconds, and I have to indicate the type of DDoS flooding (TCP Flooding, UDP Flooding or ICMP Flooding). Your help very much appreciated.</p></div><div id="comment-57612-info" class="comment-info"><span class="comment-age">(24 Nov '16, 07:39)</span> <span class="comment-user userinfo">MaryR</span></div></div><span id="57625"></span><div id="comment-57625" class="comment"><div id="post-57625-score" class="comment-score"></div><div class="comment-text"><p>The second solution works well, I just added "&gt;&gt;" so the output file is not overwritten but appended instead. As I mentioned before, I would like to keep the other fields (timestamp and TCP/UPD) on the final output file, is that possible? Thanks again.</p></div><div id="comment-57625-info" class="comment-info"><span class="comment-age">(24 Nov '16, 22:10)</span> <span class="comment-user userinfo">MaryR</span></div></div></div><div id="comment-tools-57595" class="comment-tools"></div><div class="clear"></div><div id="comment-57595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

