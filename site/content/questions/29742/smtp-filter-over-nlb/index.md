+++
type = "question"
title = "SMTP Filter over NLB"
description = '''Hi, I am trying to filter packets using Wireshark 1.10.5. but am facing some issues and need help. I have two IIS web servers &quot;A&quot; (Primary) and &quot;B&quot; on NLB which has shared web application hosted on it. These web applications sends out mails to users via a smtp mail server and I need to capture this ...'''
date = "2014-02-12T01:48:00Z"
lastmod = "2014-02-12T03:56:00Z"
weight = 29742
keywords = [ "smtp" ]
aliases = [ "/questions/29742" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SMTP Filter over NLB](/questions/29742/smtp-filter-over-nlb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29742-score" class="post-score" title="current number of votes">0</div><span id="post-29742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to filter packets using Wireshark 1.10.5. but am facing some issues and need help. I have two IIS web servers "A" (Primary) and "B" on NLB which has shared web application hosted on it. These web applications sends out mails to users via a smtp mail server and I need to capture this mails.</p><p>I set simple capture filter on both the servers for "host &lt;ipaddressofsmtpmailserver&gt;". While I can see the imf messages packets on "B"(and traffic to and from the mailserver to "B"), I get to see only one way traffic on "A"(from mailserver). I am not sure if NLB is the reason . What's wrong?</p><p>Thanks Amit</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smtp" rel="tag" title="see questions tagged &#39;smtp&#39;">smtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '14, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/4161c57af694a036461891169d8feae6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amitcumar&#39;s gravatar image" /><p><span>amitcumar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amitcumar has no accepted answers">0%</span></p></div></div><div id="comments-container-29742" class="comments-container"></div><div id="comment-tools-29742" class="comment-tools"></div><div class="clear"></div><div id="comment-29742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29752"></span>

<div id="answer-container-29752" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29752-score" class="post-score" title="current number of votes">0</div><span id="post-29752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>While I can see the imf messages packets on "B"(and traffic to and from the mailserver to "B"), I get to <strong>see only one way traffic on "A"(from mailserver)</strong>.</p></blockquote><p>that's how NLB works. All nodes have the same IP address (with shared cluster MAC addresses) and thus all nodes get the same incoming traffic. One node handles the packet (if the session is in its session table) and all other nodes simply drop that packet. The same holds true for all other nodes. That's how traffic is distributed to all nodes.</p><p>See the following links for more information</p><blockquote><p><a href="https://blogs.technet.com/b/networking/archive/2008/10/01/nlb-101-how-nlb-balances-network-traffic.aspx">https://blogs.technet.com/b/networking/archive/2008/10/01/nlb-101-how-nlb-balances-network-traffic.aspx</a><br />
<a href="http://technet.microsoft.com/en-us/library/cc725691.aspx">http://technet.microsoft.com/en-us/library/cc725691.aspx</a><br />
</p></blockquote><p>So, in a NLB cluster, you will always see the whole incoming traffic on <strong>all nodes</strong>, but the outgoing traffic only on the node that sends something.</p><p>Why you don't see any <strong>outgoing SMTP traffic on node A</strong> could have several reasons</p><ul><li>node A simply does not send any mails (bug in the software, smtp service crashed, etc.)</li><li>all clients have the same source address (Proxy or NAT) and thus NLB 'balances' them all to the same node, in your case node B</li><li>etc.</li></ul><blockquote><p>What's wrong?</p></blockquote><p>I don't know ;-)</p><ul><li>What happens if you telnet to the SMTP server on port 25 from node A (<code>telnet 1.2.3.4 25</code>)? Do you see that traffic on node A in Wireshark?</li><li>Is the SMTP service working properly on node A?</li><li>How is the HTTP traffic distributed to the nodes (see NLB statistics)? Maybe everything ends up on node B and thus node A has nothing to send via SMTP. Maybe NLB is even configured to work in that way: Everything to node B, until it dies, then everything to node A.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Feb '14, 02:53</strong> </span></p></div></div><div id="comments-container-29752" class="comments-container"><span id="29754"></span><div id="comment-29754" class="comment"><div id="post-29754-score" class="comment-score"></div><div class="comment-text"><p>Kurt, I must thank you for the quick comment.</p><p>Let me add some more details to the issue - On node A, I can see the SMTP traffic with acknowledgement/response and new mail message ID(generated from the SMTP Server), But can't see the IMFs.</p><p>"but the outgoing traffic only on the node that sends something." - I have verified that the traffic was sent out from node A but still the capture did not show this.</p><p>I have verified with telnet from both the nodes A and B respectively and am successfully able to send out mail from both the nodes individually. The network capture for this (and without any filter) on node A still captures only oneway acknowledgement(incoming) and ARP traffic only, while node B shows both incoming and outgoing. One important observation, when I drainstop node B, I start seeing both way traffic on node A.</p></div><div id="comment-29754-info" class="comment-info"><span class="comment-age">(12 Feb '14, 03:24)</span> <span class="comment-user userinfo">amitcumar</span></div></div><span id="29755"></span><div id="comment-29755" class="comment"><div id="post-29755-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The network capture for this (and without any filter) on node A still captures only oneway acknowledgement(incoming) and ARP traffic only, while node B shows both incoming and outgoing.</p></blockquote><p>interesting.</p><p>is it possible to post the capture file of both telnet sessions (port 25) from node a and node b (google drive, dropbox, cloudshark.org)?</p></div><div id="comment-29755-info" class="comment-info"><span class="comment-age">(12 Feb '14, 03:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29756"></span><div id="comment-29756" class="comment"><div id="post-29756-score" class="comment-score"></div><div class="comment-text"><p>BTW: are the two nodes <strong>absolutely identical</strong> (same hardware, same software, same OS, same patches, etc.)?</p></div><div id="comment-29756-info" class="comment-info"><span class="comment-age">(12 Feb '14, 03:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29752" class="comment-tools"></div><div class="clear"></div><div id="comment-29752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

