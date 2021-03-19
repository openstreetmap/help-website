+++
type = "question"
title = "Expert Info: &quot;Time to Live != 255&quot; message just when HSRP is Version 2"
description = '''Hi all,  this is the architecture : Switch A -&amp;gt; Interface Vlan X -&amp;gt; HSRP Version 1 -&amp;gt; PC A In the wireshark capture taken by PC A :  In the expert info there are no Notes related to the &quot;Time To live&quot;. The TTL of HSRP 1 is 1.  Switch A -&amp;gt; Interface Vlan Y -&amp;gt; HSRP Version 2 -&amp;gt; PC B ...'''
date = "2015-03-25T07:54:00Z"
lastmod = "2015-03-25T17:10:00Z"
weight = 40840
keywords = [ "hsrp-ttl" ]
aliases = [ "/questions/40840" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Expert Info: "Time to Live != 255" message just when HSRP is Version 2](/questions/40840/expert-info-time-to-live-255-message-just-when-hsrp-is-version-2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40840-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, this is the architecture :</p><p><strong>Switch A -&gt; Interface Vlan X -&gt; HSRP Version 1 -&gt; PC A</strong></p><p>In the wireshark capture taken by PC A :</p><ul><li>In the expert info there are no Notes related to the "Time To live".</li><li>The TTL of HSRP 1 is 1.</li></ul><p><strong>Switch A -&gt; Interface Vlan Y -&gt; HSRP Version 2 -&gt; PC B</strong></p><p>In the wireshark capture taken by PC B :</p><ul><li>In the expert info, in the Notes sheet there is the note : "Time To Live" !=255 for a packet sent to the Local Network Control Block (see RFC 3171).</li><li>The TTL of HSRP 2 is 1</li></ul><p>Question : Why the capture of the PC B shows me this TTL info even if is correct and present in the pcap that the HSRP-TTL is 1 ?</p></div><div id="question-tags" class="tags-container tags">hsrp-ttl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '15, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/bba638c3a54975c52c98530defa199af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ValerioItaly&#39;s gravatar image" /><p>ValerioItaly<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ValerioItaly has no accepted answers">0%</span></p></div></div><div id="comments-container-40840" class="comments-container"></div><div id="comment-tools-40840" class="comment-tools"></div><div class="clear"></div><div id="comment-40840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40864"></span>

<div id="answer-container-40864" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40864-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to the Wireshark code and your capture file, the expert info is wrong for your case, because the expert module is just looking at the IP address (224.0.0.102) which is usually tied to Cisco GLBP, where the TTL is expected to be 255 (like VRRP). Your sample frame is actually HSRP, using the same IP address (224.0.0.102), however with a TTL of 1 (which is expected for HSRP).</p><p>So, the Wireshark expert is triggering on the IP address (224.0.0.102) with a "wrong" TTL (expected:255, real:1).</p><p>Either you reconfigure your HSRP routers to use a different IP address, or you simply ignore the Wireshark expert message.</p><p>File: packet-ip.c</p><pre><code>#define IPLOCAL_NETWRK_CTRL_BLK_GLPB_ADDR       0xE0000066  &lt;=== 224.0.0.102
#define IPLOCAL_NETWRK_CTRL_BLK_GLPB_TTL        0XFF        &lt;=== TTL = 255

  if (is_a_local_network_control_block_addr(dst32)) {
    ttl = local_network_control_block_addr_valid_ttl(dst32);   &lt;=== HERE
    if (ttl != iph-&gt;ip_ttl &amp;&amp; ttl != IPLOCAL_NETWRK_CTRL_BLK_ANY_TTL) {
      expert_add_info_format(pinfo, ttl_item, &amp;ei_ip_ttl_lncb, &quot;\&quot;Time To Live\&quot; != %d for a packet sent to the &quot;
                             &quot;Local Network Control Block (see RFC 3171)&quot;,
                             ttl);
    }

local_network_control_block_addr_valid_ttl(guint32 addr)
{
  /* An exception list, as some protocols seem to insist on
   * doing differently:
   */

  /* Cisco&#39;s GLPB */
  if (IPLOCAL_NETWRK_CTRL_BLK_GLPB_ADDR == addr)    &lt;=== HERE
    return IPLOCAL_NETWRK_CTRL_BLK_GLPB_TTL;</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '15, 17:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40864" class="comments-container"><span id="40875"></span><div id="comment-40875" class="comment"><div id="post-40875-score" class="comment-score"></div><div class="comment-text"><p>Ok Kurt, your answer in very clear ! Thanks a lot to you and to SYN Bit for the support :)</p></div><div id="comment-40875-info" class="comment-info"><span class="comment-age">(26 Mar '15, 00:00)</span> ValerioItaly</div></div></div><div id="comment-tools-40864" class="comment-tools"></div><div class="clear"></div><div id="comment-40864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40855"></span>

<div id="answer-container-40855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40855-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the source code, there are a couple of multicast mac addresses in the Local Network Control Block (224.0.0.0/24) that do not have a TTL of 1. It looks like your trace of HSRP 2 traffic is matching one of the exceptions. Are you able to post a small capture file with the HSRP 2 packets (on <a href="https://appliance.cloudshark.org/upload/">Cloudshark</a> for instance), it would be easier to determine if there is a bug in the wireshark code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '15, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40855" class="comments-container"><span id="40857"></span><div id="comment-40857" class="comment"><div id="post-40857-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your support.</p><p>Here you can find an example of what I see :</p><p><a href="https://www.cloudshark.org/captures/a41f1b374661">https://www.cloudshark.org/captures/a41f1b374661</a></p></div><div id="comment-40857-info" class="comment-info"><span class="comment-age">(25 Mar '15, 13:46)</span> ValerioItaly</div></div></div><div id="comment-tools-40855" class="comment-tools"></div><div class="clear"></div><div id="comment-40855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

