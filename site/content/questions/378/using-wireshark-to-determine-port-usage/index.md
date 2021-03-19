+++
type = "question"
title = "Using Wireshark to determine port usage"
description = '''Hi all, We are interested in developing a baseline for our network traffic between sites. This will be used to create port-based ACLs on the routers.  In order to reduce the size of our captures, we are planning to use a capture filter to look for SYN packets. However, ideally the end-game is to hav...'''
date = "2010-09-30T12:12:00Z"
lastmod = "2010-10-08T10:50:00Z"
weight = 378
keywords = [ "filter", "syn" ]
aliases = [ "/questions/378" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using Wireshark to determine port usage](/questions/378/using-wireshark-to-determine-port-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-378-score" class="post-score" title="current number of votes">0</div><span id="post-378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>We are interested in developing a baseline for our network traffic between sites. This will be used to create port-based ACLs on the routers.<br />
</p><p>In order to reduce the size of our captures, we are planning to use a capture filter to look for SYN packets. However, ideally the end-game is to have a list of ports for each site and therefore we only need ONE SYN packet for each IP address/port pair. I can massage the data after the capture, but I'm wondering if anyone has any advice of clever and easy ways to do this in Wireshark.</p><p>Thanks, - Steve</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '10, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/40dc08231c522721969c22a2f630aa36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RSteveKadish&#39;s gravatar image" /><p><span>RSteveKadish</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RSteveKadish has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-378" class="comments-container"></div><div id="comment-tools-378" class="comment-tools"></div><div class="clear"></div><div id="comment-378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="379"></span>

<div id="answer-container-379" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-379-score" class="post-score" title="current number of votes">2</div><span id="post-379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RSteveKadish has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is something that Wireshark can't do, but fortunately, tshark can. Tshark is part of the CLI tools that are installed too when you install Wireshark.</p><p>You can use the following:</p><pre><code>tshark -nlr &lt;capture-file&gt; -R &quot;tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0&quot; -T fields -e ip.dst -e tcp.dstport | sort | uniq</code></pre><p>If you also would like to know from which IP's the traffic is coming from, you can use:</p><pre><code>tshark -nlr &lt;capture-file&gt; -R &quot;tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0&quot; -T fields -e ip.src -e ip.dst -e tcp.dstport | sort | uniq</code></pre><p>And if you are interested in how often sessions are set up, just add "-c" at the end. If you would like to have a top 10 of destination host/ports, you can use:</p><pre><code>tshark -nlr &lt;capture-file&gt; -R &quot;tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0&quot; -T fields -e ip.dst -e tcp.dstport | sort | uniq -c | sort -rn | head</code></pre><p>(if you use windows, these commands can be used within a cygwin shell, have a look at http://www.cygwin.com)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '10, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-379" class="comments-container"><span id="381"></span><div id="comment-381" class="comment"><div id="post-381-score" class="comment-score"></div><div class="comment-text"><p>Hi Sake,</p><p>Thanks very much! This is great info.</p><p>I already have a capture running with the tcp[0xd]&amp;18=2 filter (because there simply isn't going to be enough disk space for a full capture.) So I assume that I should use the tshark syntaxes you provided and just leave out the -R option?</p><p>Thanks, - Steve</p></div><div id="comment-381-info" class="comment-info"><span class="comment-age">(30 Sep '10, 13:00)</span> <span class="comment-user userinfo">RSteveKadish</span></div></div><span id="382"></span><div id="comment-382" class="comment"><div id="post-382-score" class="comment-score"></div><div class="comment-text"><p>Sure thing, if the tracefile only contains the SYN-packets, it's not needed to filter for SYN-packets again :-)</p></div><div id="comment-382-info" class="comment-info"><span class="comment-age">(30 Sep '10, 13:03)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="460"></span><div id="comment-460" class="comment"><div id="post-460-score" class="comment-score"></div><div class="comment-text"><p>Hi Sake,</p><p>I wanted to let you know that I played around with these commands (after a week of capturing) and they are extremely helpful. They will save me a lot of work by not having to massage the data manually.</p><p>Best, - Steve</p></div><div id="comment-460-info" class="comment-info"><span class="comment-age">(08 Oct '10, 07:32)</span> <span class="comment-user userinfo">RSteveKadish</span></div></div><span id="464"></span><div id="comment-464" class="comment"><div id="post-464-score" class="comment-score"></div><div class="comment-text"><p>Glad this worked for you! And thanks for the feedback :-)</p></div><div id="comment-464-info" class="comment-info"><span class="comment-age">(08 Oct '10, 10:50)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-379" class="comment-tools"></div><div class="clear"></div><div id="comment-379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

