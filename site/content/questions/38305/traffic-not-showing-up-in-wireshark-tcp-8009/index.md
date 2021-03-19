+++
type = "question"
title = "Traffic not showing up in Wireshark (TCP 8009)"
description = '''I have a VMware View Security server that periodically &#x27;pings&#x27; or communicates to a View Connect server on 8009. There are connections shown in Netstat:  [ws_TunnelService.exe]  TCP 10.3.0.13:55487 10.1.0.21:4001 ESTABLISHED  [ws_TunnelService.exe]  TCP 10.3.0.13:55764 10.1.0.21:8009 ESTABLISHED  Th...'''
date = "2014-12-03T07:44:00Z"
lastmod = "2014-12-03T07:44:00Z"
weight = 38305
keywords = [ "tomcat", "vmware", "view" ]
aliases = [ "/questions/38305" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Traffic not showing up in Wireshark (TCP 8009)](/questions/38305/traffic-not-showing-up-in-wireshark-tcp-8009)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38305-score" class="post-score" title="current number of votes">0</div><span id="post-38305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a VMware View Security server that periodically 'pings' or communicates to a View Connect server on 8009. There are connections shown in Netstat:</p><pre><code>    [ws_TunnelService.exe]
  TCP    10.3.0.13:55487        10.1.0.21:4001         ESTABLISHED
 [ws_TunnelService.exe]
  TCP    10.3.0.13:55764        10.1.0.21:8009         ESTABLISHED</code></pre><p>The port 4001 traffic shows up in a wireshark trace:</p><pre><code>238 26.776074000    10.1.0.21   10.3.0.13   TCP 73  4001→53416 [PSH, ACK] Seq=30 Ack=135 Win=4025 Len=19
239 26.778194000    10.3.0.13   10.1.0.21   TCP 2814    53416→4001 [ACK] Seq=135 Ack=49 Win=32597 Len=2760</code></pre><p>But the 8009 traffic does not. I do tcp.port=8009 filter and get nothing. I have evidence that traffic should be going across in a view log file (from the 10.3.0.13 server):</p><pre><code>2014-12-02T20:10:05.271-05:00 DEBUG (0550-0484) &lt;AJP connection pool monitor&gt; [a] /10.1.0.21:8009
2014-12-02T20:10:05.271-05:00 TRACE (0550-0484) &lt;AJP connection pool monitor&gt; [b] Fetching connection from pool: /10.1.0.21:8009
2014-12-02T20:10:05.271-05:00 TRACE (0550-0484) &lt;AJP connection pool monitor&gt; [b] Total pool size: 5
2014-12-02T20:10:05.271-05:00 TRACE (0550-0484) &lt;AJP connection pool monitor&gt; [b] Sending test CPing request...
2014-12-02T20:10:05.474-05:00 TRACE (0550-0484) &lt;AJP connection pool monitor&gt; [b] Received test CPong.
2014-12-02T20:10:05.474-05:00 TRACE (0550-0484) &lt;AJP connection pool monitor&gt; [b] Returning connection to pool: /10.1.0.21:8009
2014-12-02T20:10:05.474-05:00 TRACE (0550-0484) &lt;AJP connection pool monitor&gt; [b] Total pool size: 6</code></pre><p>It looks like the traffic is being tunneled... but my question is why is the 4001 traffic showing up in a trace and the 8009 is not??</p><p>Thanks much for any ideas. I can provide more info if needed...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tomcat" rel="tag" title="see questions tagged &#39;tomcat&#39;">tomcat</span> <span class="post-tag tag-link-vmware" rel="tag" title="see questions tagged &#39;vmware&#39;">vmware</span> <span class="post-tag tag-link-view" rel="tag" title="see questions tagged &#39;view&#39;">view</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '14, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/cae949684b0fa2e07310d5f1f7af3cef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hatari&#39;s gravatar image" /><p><span>hatari</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hatari has no accepted answers">0%</span></p></div></div><div id="comments-container-38305" class="comments-container"></div><div id="comment-tools-38305" class="comment-tools"></div><div class="clear"></div><div id="comment-38305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

