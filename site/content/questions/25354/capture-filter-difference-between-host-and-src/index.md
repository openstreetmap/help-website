+++
type = "question"
title = "Capture filter - -difference between &quot;host&quot; and &quot;Src&quot;"
description = '''Hi I&#x27;m interested to capture all data leaving certain hosts we are spanning. I&#x27;m only interested in the data transmitted from the hosts (either a conversation initiated from the host or a response packet). When I try a filter using &quot;Src x.x.x.x - it appears to work in that I only see traffic with my...'''
date = "2013-09-29T21:21:00Z"
lastmod = "2013-09-29T23:20:00Z"
weight = 25354
keywords = [ "src", "host", "capture-filter" ]
aliases = [ "/questions/25354" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter - -difference between "host" and "Src"](/questions/25354/capture-filter-difference-between-host-and-src)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25354-score" class="post-score" title="current number of votes">0</div><span id="post-25354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I'm interested to capture all data leaving certain hosts we are spanning. I'm only interested in the data transmitted from the hosts (either a conversation initiated from the host or a response packet). When I try a filter using "Src x.x.x.x - it appears to work in that I only see traffic with my filtered src address, however I believe I not seeing a bunch of traffic which I should be as when I use the "host x.x.x.x" filter i see a lot more traffic to other IPs which don't appear in the "src" filter capture. Any ideas - its seems very strange - itsw almost like I am seeing a subnet of the outbound traffic to a select group of dst IPs only with the "src" filter in place.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-src" rel="tag" title="see questions tagged &#39;src&#39;">src</span> <span class="post-tag tag-link-host" rel="tag" title="see questions tagged &#39;host&#39;">host</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '13, 21:21</strong></p><img src="https://secure.gravatar.com/avatar/6389c211ec05b85529186bd45d63fd6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="murawai&#39;s gravatar image" /><p><span>murawai</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="murawai has no accepted answers">0%</span></p></div></div><div id="comments-container-25354" class="comments-container"></div><div id="comment-tools-25354" class="comment-tools"></div><div class="clear"></div><div id="comment-25354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25357"></span>

<div id="answer-container-25357" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25357-score" class="post-score" title="current number of votes">2</div><span id="post-25357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>difference between "host" and "Src"</p></blockquote><p>To quote the pcap-filter man page (or the tcpdump man page for earlier versions of libpcap and tcpdump):</p><pre><code>   The filter expression consists of one or more  primitives.   Primitives
   usually consist of an id (name or number) preceded by one or more qual-
   ifiers.  There are three different kinds of qualifier:

   type   qualifiers say what kind of thing the id name or  number  refers
          to.   Possible  types are host, net , port and portrange.  E.g.,
          `host foo&#39;, `net 128.3&#39;, `port 20&#39;, `portrange  6000-6008&#39;.   If
          there is no type qualifier, host is assumed.

   dir    qualifiers  specify  a  particular  transfer direction to and/or
          from id.  Possible directions are src, dst, src or dst, src  and
          dst,  addr1, addr2, addr3, and addr4.  E.g., `src foo&#39;, `dst net
          128.3&#39;, `src or dst port ftp-data&#39;.  If there is no  dir  quali-
          fier, src or dst is assumed.  The addr1, addr2, addr3, and addr4
          qualifiers are only valid for IEEE 802.11 Wireless LAN link lay-
          ers.   For  some  link  layers,  such as SLIP and the ``cooked&#39;&#39;
          Linux capture mode used for the  ``any&#39;&#39;  device  and  for  some
          other  device  types, the inbound and outbound qualifiers can be
          used to specify a desired direction.

              ...

   dst host host
          True  if  the  IPv4/v6  destination field of the packet is host,
          which may be either an address or a name.

   src host host
          True if the IPv4/v6 source field of the packet is host.

   host host
          True if either the IPv4/v6 source or destination of  the  packet
          is host.

          Any of the above host expressions can be prepended with the key-
          words, ip, arp, rarp, or ip6 as in:
               ip host host
          which is equivalent to:
               ether proto \ip and host host
          If host is a name with multiple IP addresses, each address  will
          be checked for a match.</code></pre><p>So <code>host</code> <em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em> means "source or destination address is <em>xxx</em>.<em>xxx</em>.<em>xxx</em>.<em>xxx</em>", and <code>src</code> <em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em> is the same as <code>src host</code> <em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em>, which means "source address is <em>xxx</em>.<em>xxx</em>.<em>xxx</em>.<em>xxx</em>".</p><p>I.e., <code>host</code> <em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em> will match any packets from <em>or</em> to <em>xxx</em>.<em>xxx</em>.<em>xxx</em>.<em>xxx</em>, but <code>src</code> <em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em> will match any packets from <em>xxx</em>.<em>xxx</em>.<em>xxx</em>.<em>xxx</em> but will only match packets <em>to</em> <em>xxx</em>.<em>xxx</em>.<em>xxx</em>.<em>xxx</em> if they are also <em>from</em> <em>xxx</em>.<em>xxx</em>.<em>xxx</em>.<em>xxx</em>.</p><p>Therefore, <code>host</code> <em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em> will match more packets than will <code>src</code> <em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em><code>.</code><em>xxx</em>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '13, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-25357" class="comments-container"></div><div id="comment-tools-25357" class="comment-tools"></div><div class="clear"></div><div id="comment-25357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

