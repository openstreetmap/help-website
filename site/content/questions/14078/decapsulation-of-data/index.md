+++
type = "question"
title = "Decapsulation of data"
description = '''Hi Can anybody help to decapsulate only the data or payload from all other network related data, so I on a easy way, can find data transmitted from one ip address.  I have a system transmitting data, and need to extract data for display on another system I have recorded a wireshark-file, but I need ...'''
date = "2012-09-06T02:02:00Z"
lastmod = "2015-03-06T05:09:00Z"
weight = 14078
keywords = [ "decapsulation", "tshark", "data", "dataextraction", "payload" ]
aliases = [ "/questions/14078" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decapsulation of data](/questions/14078/decapsulation-of-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14078-score" class="post-score" title="current number of votes">0</div><span id="post-14078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Can anybody help to decapsulate only the data or payload from all other network related data, so I on a easy way, can find data transmitted from one ip address.</p><p>I have a system transmitting data, and need to extract data for display on another system</p><p>I have recorded a wireshark-file, but I need help to get Tshark or Wireshark to insulate or extract 'data only'.</p><p>Per</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decapsulation" rel="tag" title="see questions tagged &#39;decapsulation&#39;">decapsulation</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-dataextraction" rel="tag" title="see questions tagged &#39;dataextraction&#39;">dataextraction</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '12, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/69c5654973e4d75f51525c6557e34106?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Great%20Dane&#39;s gravatar image" /><p><span>Great Dane</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Great Dane has no accepted answers">0%</span></p></div></div><div id="comments-container-14078" class="comments-container"></div><div id="comment-tools-14078" class="comment-tools"></div><div class="clear"></div><div id="comment-14078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14140"></span>

<div id="answer-container-14140" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14140-score" class="post-score" title="current number of votes">1</div><span id="post-14140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are a number of ways to do this. One way to do this would be to open the file using Wireshark, and then right click on one of the packets of interest and choose "Follow TCP stream" or "Follow UDP stream" from the popup menu. Another way to do something like that would be to use Tshark to dump just the tcp.data or udp.data. For example, you could use a command line like this:</p><pre><code>tshark -r sample1.pcap -R &#39;tcp &amp;&amp; ip.addr==192.168.0.141&#39; -Tfields -etcp.data</code></pre>which would dump all <code>tcp.data</code> as hex strings.</div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '12, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/589ac3289099c34149c526ee7bb1a805?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eberoset&#39;s gravatar image" /><p><span>eberoset</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eberoset has no accepted answers">0%</span></p></div></div><div id="comments-container-14140" class="comments-container"><span id="14569"></span><div id="comment-14569" class="comment"><div id="post-14569-score" class="comment-score"></div><div class="comment-text"><p>Thanks.</p><p>I can add how to transfer payload data to a binary file:</p><p>tshark -V -r e:\wwireshark1.pcapng -R ip.src==192.1.1.200 -w e:\raw.bin</p><p>Great Dane</p></div><div id="comment-14569-info" class="comment-info"><span class="comment-age">(27 Sep '12, 03:55)</span> <span class="comment-user userinfo">Great Dane</span></div></div><span id="25744"></span><div id="comment-25744" class="comment"><div id="post-25744-score" class="comment-score"></div><div class="comment-text"><p>"Another way to do something like that would be to use Tshark to dump just the tcp.data or udp.data."</p><p>I found neither of these filters worked, although I did find tcp.sequence_data did. No equivalent for UDP apparently.</p><p>"... -w e:\raw.bin" Doesn't this write the whole packet, headers and all?</p></div><div id="comment-25744-info" class="comment-info"><span class="comment-age">(08 Oct '13, 06:56)</span> <span class="comment-user userinfo">wiggers</span></div></div><span id="25755"></span><div id="comment-25755" class="comment"><div id="post-25755-score" class="comment-score">1</div><div class="comment-text"><p>The field was renamed from tcp.data to tcp.segment_data in Wireshark version 1.10 and higher. Also note that that filter only works when the data <strong>isn't</strong> being dissected by some other dissector. So the way to get just that part data is a bit counterintuitive. Here's how to do it, using http traffic as an example:</p><ol><li>start Wireshark and open the dialog Analyze-&gt;Enabled Protocols...</li><li>choose the protocol or protocols you're interested in extracting (e.g. http) and <strong>disable</strong> them (no, that's not a typo!)</li><li>save that setting and exit Wireshark</li><li>run tshark as <code>tshark -r mydata.pcap -Tfields -edata</code></li><li>you might wish to go back into Wireshark and re-enable the protocol(s)</li></ol><p>What you'll get is hex dumps of only the undecoded data (which is why you disabled them). Note that this works with both TCP and UDP without change. For further details on disabling protocols, see <a href="http://ask.wireshark.org/questions/9544/how-to-disable-dissectors-in-tshark">this question and answer.</a></p></div><div id="comment-25755-info" class="comment-info"><span class="comment-age">(08 Oct '13, 11:36)</span> <span class="comment-user userinfo">beroset</span></div></div><span id="40322"></span><div id="comment-40322" class="comment"><div id="post-40322-score" class="comment-score"></div><div class="comment-text"><p>Would love to know something I can pipe these hexdumps through to get an ASCII translation. I've tried <code>xxd -r</code>, but the decode gets garbled part way through. thshark / Wireshark decode them just fine</p></div><div id="comment-40322-info" class="comment-info"><span class="comment-age">(06 Mar '15, 05:09)</span> <span class="comment-user userinfo">rosensama</span></div></div></div><div id="comment-tools-14140" class="comment-tools"></div><div class="clear"></div><div id="comment-14140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

