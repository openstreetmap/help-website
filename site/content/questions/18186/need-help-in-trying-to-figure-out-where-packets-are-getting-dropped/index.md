+++
type = "question"
title = "Need help in trying to figure out where packets are getting dropped"
description = '''We have several remote sites connecting to a central location. Each remote site has its own file and print server hosted at the central location as virtual machines. Recently, we&#x27;ve been having problems pulling data from one of these servers (e.g., getting directory listing containing large amounts ...'''
date = "2013-01-31T09:15:00Z"
lastmod = "2013-02-04T11:14:00Z"
weight = 18186
keywords = [ "packets", "dropped" ]
aliases = [ "/questions/18186" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need help in trying to figure out where packets are getting dropped](/questions/18186/need-help-in-trying-to-figure-out-where-packets-are-getting-dropped)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18186-score" class="post-score" title="current number of votes">0</div><span id="post-18186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have several remote sites connecting to a central location. Each remote site has its own file and print server hosted at the central location as virtual machines. Recently, we've been having problems pulling data from one of these servers (e.g., getting directory listing containing large amounts of files and folders), but only from machines at the central site. Users at the remote site who have been assigned this particular server have not reported any problems. All other servers have been behaving fine, and I can't see how this one server is different from the others.</p><p>Captures near the server show normal behavior until it comes time to actually send the directory contents, then there are repeated attempts to transmit the data, followed by a [RST,ACK]. Captures near the machine browsing the directory show just the [RST, ACK]. I've done captures in various points in the intervening network and I think I've found the spot where it's not sending data any further, even though all other connectivity to this machine is fine (I'm using my workstation for testing).</p><p>The last spot the retransmitted packets get to, the source and destination ips seem correct, and layer 2 info shows the source as being the switch at the remote site the packet came from, and the destination seems to be the MAC address associated with the vlan that the browsing machine is a part of. Packets seem to be dropped somewhere around this point. Captures at the interface where the packets should leave to head to the browsing machine show everything but the retransmitted packets. Again, the machine doing the browsing has normal connectivity for all other things.</p><p>How can I find out why the packets are getting dropped?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-dropped" rel="tag" title="see questions tagged &#39;dropped&#39;">dropped</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '13, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/996fea569b162f02d49fb26f37776fea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pfisterfarm&#39;s gravatar image" /><p><span>pfisterfarm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pfisterfarm has no accepted answers">0%</span></p></div></div><div id="comments-container-18186" class="comments-container"></div><div id="comment-tools-18186" class="comment-tools"></div><div class="clear"></div><div id="comment-18186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18232"></span>

<div id="answer-container-18232" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18232-score" class="post-score" title="current number of votes">0</div><span id="post-18232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Users at the remote site who have been assigned this particular server have not reported any problems.</p></blockquote><p>how do they access the server? Directly via CIFS/SMB or via a VMware View instance connected from the remote location? In general: Is the method used to access the server the <strong>same</strong> in the central location and the remote location?</p><blockquote><p>Packets seem to be dropped somewhere around this point.</p></blockquote><p>Did you check if there are <strong>jumbo frames</strong> involved (check the size of the packets, captured "near" the faulty server)? Maybe one of your switches is dropping jumbo frames and thus causing trouble.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '13, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Feb '13, 09:58</strong> </span></p></div></div><div id="comments-container-18232" class="comments-container"><span id="18293"></span><div id="comment-18293" class="comment"><div id="post-18293-score" class="comment-score"></div><div class="comment-text"><p>Yes, it's directly with CIFS/SMB in both places.</p><p>The packet size when captured near the server end is 1514.</p></div><div id="comment-18293-info" class="comment-info"><span class="comment-age">(04 Feb '13, 11:14)</span> <span class="comment-user userinfo">pfisterfarm</span></div></div></div><div id="comment-tools-18232" class="comment-tools"></div><div class="clear"></div><div id="comment-18232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

