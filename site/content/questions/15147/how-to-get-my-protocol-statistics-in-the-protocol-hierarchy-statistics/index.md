+++
type = "question"
title = "How to get my protocol statistics in the Protocol Hierarchy Statistics"
description = '''After following the steps in the tutorial i expected that the Protocol Hierarchical Statistics would have been extended with the stats details. This is not the case however. Although with tshark i can see that the details are being collected. Is there a way to expand the phs to show the details? tsh...'''
date = "2012-10-22T02:55:00Z"
lastmod = "2012-10-22T02:55:00Z"
weight = 15147
keywords = [ "phs", "stat_tree", "wireshark" ]
aliases = [ "/questions/15147" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get my protocol statistics in the Protocol Hierarchy Statistics](/questions/15147/how-to-get-my-protocol-statistics-in-the-protocol-hierarchy-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15147-score" class="post-score" title="current number of votes">0</div><span id="post-15147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After following the steps in the tutorial i expected that the Protocol Hierarchical Statistics would have been extended with the stats details. This is not the case however. Although with tshark i can see that the details are being collected. Is there a way to expand the phs to show the details?</p><pre><code>tshark -r /home/kurt/wireshark/foo_test.pcap -z foo,tree -z io,phs
OOPS: dissector table &quot;sctp.ppi&quot; doesn&#39;t exist
Protocol being registered is &quot;Datagram Transport Layer Security&quot;
Registering the register_foo_stat_trees
foo_stats_tree_init ..
queuing packet for tap 73 type 1
foo_stats_tree_packet ..
  1   0.000000     10.1.1.1 -&gt; 10.2.2.2     foo 60 Type ONE
queuing packet for tap 73 type 2
foo_stats_tree_packet ..
  2   0.000001     10.1.1.1 -&gt; 10.2.2.2     foo 60 Type TWO
queuing packet for tap 73 type 3
foo_stats_tree_packet ..
  3   0.000002     10.1.1.1 -&gt; 10.2.2.2     foo 60 Type DRIE
queuing packet for tap 73 type 4
foo_stats_tree_packet ..
  4   0.000003     10.1.1.1 -&gt; 10.2.2.2     foo 60 Type Unknown (0x04)
queuing packet for tap 73 type 0
foo_stats_tree_packet ..
  5   0.000004     10.1.1.1 -&gt; 10.2.2.2     foo 60 Type Unknown (0x00)

===================================================================
Protocol Hierarchy Statistics
Filter:

eth                                      frames:5 bytes:300
  ip                                     frames:5 bytes:300
    udp                                  frames:5 bytes:300
      foo                                frames:5 bytes:300
===================================================================

===================================================================
 Foo Protocol/Packet Types        value         rate         percent
-------------------------------------------------------------------
 Total Packets                       5    1249.999941                
  FOO Packet Types                    5    1249.999941         100.00%
   ONE                                 1     249.999988          20.00%
   TWO                                 1     249.999988          20.00%
   DRIE                                1     249.999988          20.00%
   Unknown packet type (4)             1     249.999988          20.00%
   Unknown packet type (0)             1     249.999988          20.00%

===================================================================</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-phs" rel="tag" title="see questions tagged &#39;phs&#39;">phs</span> <span class="post-tag tag-link-stat_tree" rel="tag" title="see questions tagged &#39;stat_tree&#39;">stat_tree</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '12, 02:55</strong></p><img src="https://secure.gravatar.com/avatar/e1ee227f42dda97ad84d4ad6a58fe957?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KurtDP&#39;s gravatar image" /><p><span>KurtDP</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KurtDP has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '12, 06:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-15147" class="comments-container"></div><div id="comment-tools-15147" class="comment-tools"></div><div class="clear"></div><div id="comment-15147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

