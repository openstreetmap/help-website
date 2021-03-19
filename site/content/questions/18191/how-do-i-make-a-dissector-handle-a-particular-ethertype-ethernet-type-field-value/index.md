+++
type = "question"
title = "How do I make a dissector handle a particular EtherType (Ethernet type field) value?"
description = '''I have a custom packet that can be encapsulated in a TCP/IP or Ethernet protocol. The problem im having is adding my heuristic dissector in at the lowest level so the TCP/IP and Ethernet sections of the packets are decoded by their respective dissectors first before coming to my dissector.  If i use...'''
date = "2013-01-31T14:46:00Z"
lastmod = "2013-01-31T20:35:00Z"
weight = 18191
keywords = [ "ethertype", "dissector", "ethernet" ]
aliases = [ "/questions/18191" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I make a dissector handle a particular EtherType (Ethernet type field) value?](/questions/18191/how-do-i-make-a-dissector-handle-a-particular-ethertype-ethernet-type-field-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18191-score" class="post-score" title="current number of votes">0</div><span id="post-18191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a custom packet that can be encapsulated in a TCP/IP or Ethernet protocol. The problem im having is adding my heuristic dissector in at the lowest level so the TCP/IP and Ethernet sections of the packets are decoded by their respective dissectors first before coming to my dissector.</p><p>If i use <code>heur_dissector_add("eth",(heur_dissector_t) dissect_PROTONAME, proto_PROTONAME);</code> it adds it in at the ethernet level but because the eth dissector tries all the heuristic dissectors first before it tries itself the destination and source MAC addresses aren't decoded. I've tried calling the "eth" dissector before my code runs but because of what i mentioned earlier it gets stuck in an infinite loop. I'd rather not have to decode the destination and source MAC addresses as this will cause my code to be unusable if the packet comes in wrapped in tcp/ip.</p><p>Is there any way to add my heuristic dissector in just before the "data dissector"?. I'm yet to find anything that lists all the different levels/types of heuristic dissectors....the only ones i've found are, "eth", "tcp", "udp" and a couple of others that haven't helped</p><p>thanks in advance for the help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethertype" rel="tag" title="see questions tagged &#39;ethertype&#39;">ethertype</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '13, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/024c038a84faf77c618cfe43ee97ed64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StealthUE&#39;s gravatar image" /><p><span>StealthUE</span><br />
<span class="score" title="66 reputation points">66</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StealthUE has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Feb '13, 17:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-18191" class="comments-container"><span id="18193"></span><div id="comment-18193" class="comment"><div id="post-18193-score" class="comment-score"></div><div class="comment-text"><p>Does your protocol have a specific Ethernet type value that you've either registered with the IEEE or are using despite that? If so, the right answer is not to use a heuristic dissector, but to register your dissector in the "ethertype" table using the Ethernet type value.</p></div><div id="comment-18193-info" class="comment-info"><span class="comment-age">(31 Jan '13, 17:04)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18194"></span><div id="comment-18194" class="comment"><div id="post-18194-score" class="comment-score"></div><div class="comment-text"><p>Cirrus Cobranet Packet. How would I go about registering the dissector in the "ethertype" table?. My protocol can come in as either an (1) ethernet packet-&gt;my protocol or (2) ethernet packet-&gt;ip packet-&gt;my protocol. Would registering it in the "ethertype" table cause my dissector to reject the second type?</p></div><div id="comment-18194-info" class="comment-info"><span class="comment-age">(31 Jan '13, 17:23)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18195"></span><div id="comment-18195" class="comment"><div id="post-18195-score" class="comment-score"></div><div class="comment-text"><p>"Ethernet II" isn't an Ethernet type value; I'm referring to <a href="http://standards.ieee.org/develop/regauth/ethertype/index.html">EtherType values</a>.</p></div><div id="comment-18195-info" class="comment-info"><span class="comment-age">(31 Jan '13, 17:37)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18196"></span><div id="comment-18196" class="comment"><div id="post-18196-score" class="comment-score"></div><div class="comment-text"><p>sorry my bad, i edited it but it must not have refreshed for you. Cirrus Cobranet Packet 0x8819</p></div><div id="comment-18196-info" class="comment-info"><span class="comment-age">(31 Jan '13, 17:40)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18197"></span><div id="comment-18197" class="comment"><div id="post-18197-score" class="comment-score"></div><div class="comment-text"><p>inside my protocol there is also another type thats consistently used, 0x8401 but it's not a registered ethertype value. Can you point me to an example that registers its own ethertype value??</p></div><div id="comment-18197-info" class="comment-info"><span class="comment-age">(31 Jan '13, 17:49)</span> <span class="comment-user userinfo">StealthUE</span></div></div></div><div id="comment-tools-18191" class="comment-tools"></div><div class="clear"></div><div id="comment-18191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18199"></span>

<div id="answer-container-18199" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18199-score" class="post-score" title="current number of votes">5</div><span id="post-18199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, then to dissect packets with an EtherType of 0x8819 with your dissector, and have the Ethernet dissector dissect the destination address, source address, and EtherType/length field and hand your dissector the Ethernet payload (i.e., the tvbuff handed to your dissector starts with the first byte of the payload, <em>not</em> the first byte of the destination address, and it includes neither the destination address, the source address, or the EtherType/length field), what you would do is:</p><ul><li>create a handle for your dissector;</li><li>call <code>dissector_add_uint("ethertype", 0x8819,</code> <em>my_handle</em><code>);</code> in your dissector's handoff routine.</li></ul><p>As for whatever Cobranet-over-IP encapsulation you're using (Cirrus Logic <a href="http://www.cobranet.info/technology/faq#Q26">seems pretty insistent that they <em>don't</em> use IP</a>):</p><ul><li>if it runs over raw IP, if you have an IP protocol number assigned to it, you could register in the "ip.proto" dissector table with that protocol number value - your dissector wouldn't be heuristic, and registering it in both the "ethertype" and "ip.proto" tables will not cause any problems (it will be recognized in both cases);</li><li>if it runs over TCP or UDP, you would either register it with a fixed (or configurable) port number ("tcp.port" or "udp.port"), in which case it wouldn't be heuristic and, again, would not have a problem with the "ethertype" registration, or you would register a heuristic dissector for TCP or UDP, in which case you would need two separate dissector functions, a non-heuristic one used for EtherType 0x8819 and a heuristic one that checks whether the packet is a Cobranet packet and then calls the non-heuristic one if the packet is a Cobranet packet.</li></ul><p>As for 0x8401, there's "registered" in the sense of "registered with the IEEE", which requires $2,825 US and possibly as much as 97 days (or more if they have questions), and there's "registered" in the sense of "registered in the "ethernet" table of Wireshark. Wireshark doesn't know, or care, whether you've registered an Ethernet type with the IEEE, although dissectors that register an EtherType value in the "ethertype" table when that EtherType value isn't "registered" with the IEEE might not be accepted into the official Wireshark source code base if submitted for inclusion. For that one, you'd make a call to <code>dissector_add_uint()</code> the same way you'd make a call for an EtherType officially registered with the IEEE.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '13, 17:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jan '13, 18:05</strong> </span></p></div></div><div id="comments-container-18199" class="comments-container"><span id="18200"></span><div id="comment-18200" class="comment"><div id="post-18200-score" class="comment-score"></div><div class="comment-text"><p>you sir are a genius!. thanks heaps. I'll give this a go :). Ive read almost every bit of documentation on dissecting packets in wireshark and have yet to come across this information. thanks again...saved me heaps of time</p></div><div id="comment-18200-info" class="comment-info"><span class="comment-age">(31 Jan '13, 18:03)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18201"></span><div id="comment-18201" class="comment"><div id="post-18201-score" class="comment-score"></div><div class="comment-text"><p><code>dissector_add_uint()</code> is discussed in <code>doc/README.developer</code>, but it doesn't specifically mention the "ethertype" dissector table there.</p></div><div id="comment-18201-info" class="comment-info"><span class="comment-age">(31 Jan '13, 18:07)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18208"></span><div id="comment-18208" class="comment"><div id="post-18208-score" class="comment-score"></div><div class="comment-text"><p>hey, this is what i have so far. It's not picking up the packets...not sure why</p><pre><code>/* packet-MYPROTOCOL.c
 * Routines for MYPROTOCOL dissection
 */

#ifdef HAVE_CONFIG_H
# include &quot;config.h&quot;
#endif

#if 0
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#endif

#include &lt;epan/packet.h&gt;
#include &lt;epan/prefs.h&gt;

void proto_reg_handoff_MYPROTOCOL(void);

static int proto_MYPROTOCOL = -1;
static int hf_MYPROTOCOL_data = -1;

static gboolean gPREF_HEX = FALSE;

static gint ett_MYPROTOCOL = -1;

static int
dissect_MYPROTOCOL(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    proto_item *ti;
    proto_tree *MYPROTOCOL_tree;

    if ( tvb_get_guint8(tvb,-2) != 0x84 )
        return (FALSE);
    if ( tvb_get_guint8(tvb,-1) != 0x01 )
        return (FALSE);

    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;MYPROTOCOL&quot;);
    col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;XXX Request&quot;);

    if (tree) {
        ti = proto_tree_add_item(tree, proto_MYPROTOCOL, tvb, 0, -1, ENC_NA);

        MYPROTOCOL_tree = proto_item_add_subtree(ti, ett_MYPROTOCOL);

        proto_tree_add_item(MYPROTOCOL_tree, hf_MYPROTOCOL_data, tvb, 0, -1, ENC_NA);
    }
}

void
proto_register_MYPROTOCOL(void)
{
    module_t *MYPROTOCOL_module;

    static hf_register_info hf[] = {
        { &amp;hf_MYPROTOCOL_data,
            { &quot;MYPROTOCOL Data&quot;, &quot;MYPROTOCOL.data&quot;, FT_NONE, BASE_NONE, NULL, 0x0, &quot;MYPROTOCOL Data Collected&quot;, HFILL }
        }
    };

    static gint *ett[] = {
        &amp;ett_MYPROTOCOL
    };

    proto_MYPROTOCOL = proto_register_protocol(&quot;MYPROTOCOL&quot;, &quot;MYPROTOCOL&quot;, &quot;MYPROTOCOL&quot;);

    proto_register_field_array(proto_MYPROTOCOL, hf, array_length(hf));
    proto_register_subtree_array(ett, array_length(ett));

    MYPROTOCOL_module = prefs_register_protocol(proto_MYPROTOCOL, proto_reg_handoff_MYPROTOCOL);

    prefs_register_bool_preference(MYPROTOCOL_module, &quot;show_hex&quot;,
     &quot;Display numbers in Hex&quot;,
         &quot;Enable to display numerical values in hexadecimal.&quot;,
         &amp;gPREF_HEX);
}

void
proto_reg_handoff_MYPROTOCOL(void)
{
    static gboolean initialized = FALSE;

    if (!initialized) {
        static dissector_handle_t MYPROTOCOL_handle;
        MYPROTOCOL_handle = create_dissector_handle((dissector_t)dissect_MYPROTOCOL, proto_MYPROTOCOL);
        dissector_add_uint(&quot;ethertype&quot;, 0x8401, MYPROTOCOL_handle);
    }
}</code></pre><p>This is what my packet looks like [Dest. MAC Addr][Source MAC Addr][Cobranet packet identifier][0x84][0x01][DATA to process]</p><p>any help is appreciated :)</p></div><div id="comment-18208-info" class="comment-info"><span class="comment-age">(31 Jan '13, 19:18)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18209"></span><div id="comment-18209" class="comment"><div id="post-18209-score" class="comment-score"></div><div class="comment-text"><p>hey Guy Harris, can you have a look at the code below and tell me what im doing wrong..thanks</p></div><div id="comment-18209-info" class="comment-info"><span class="comment-age">(31 Jan '13, 19:27)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18210"></span><div id="comment-18210" class="comment"><div id="post-18210-score" class="comment-score"></div><div class="comment-text"><p>i also tried changing the index values in tvb_get_guint8(tvb,INDEX) but it didnt change anything</p></div><div id="comment-18210-info" class="comment-info"><span class="comment-age">(31 Jan '13, 19:32)</span> <span class="comment-user userinfo">StealthUE</span></div></div><span id="18213"></span><div id="comment-18213" class="comment not_top_scorer"><div id="post-18213-score" class="comment-score"></div><div class="comment-text"><blockquote><p>This is what my packet looks like [Dest. MAC Addr][Source MAC Addr][Cobranet packet identifier][0x84][0x01][DATA to process]</p></blockquote><p>If by "Cobranet packet identifier" you mean 0x8819, then that's the EtherType of the packet, <em>not</em> 0x8401, and it's not capturing the packets because you didn't do</p><pre><code>dissector_add_uint(&quot;ethertype&quot;, 0x8819, MYPROTOCOL_handle);</code></pre><p>so that your dissector will be called for an EtherType of 0x8819.</p></div><div id="comment-18213-info" class="comment-info"><span class="comment-age">(31 Jan '13, 20:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18215"></span><div id="comment-18215" class="comment not_top_scorer"><div id="post-18215-score" class="comment-score"></div><div class="comment-text"><p>ahhhhh, thanks man</p></div><div id="comment-18215-info" class="comment-info"><span class="comment-age">(31 Jan '13, 20:35)</span> <span class="comment-user userinfo">StealthUE</span></div></div></div><div id="comment-tools-18199" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-18199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

