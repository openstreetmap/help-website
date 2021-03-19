+++
type = "question"
title = "How do I have my dissector handle a protocol running on top of UDP?"
description = '''Hi all, I&#x27;m using tshark for some specific dissectors. I have to modify the function dissect_data(...) in packet-data.c. In my scenario, most of the packet must go through this function. My objective is: at the end of this function, I want to clear all data of this packet before going to the next in...'''
date = "2014-12-24T20:30:00Z"
lastmod = "2014-12-27T15:37:00Z"
weight = 38703
keywords = [ "udp" ]
aliases = [ "/questions/38703" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I have my dissector handle a protocol running on top of UDP?](/questions/38703/how-do-i-have-my-dissector-handle-a-protocol-running-on-top-of-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38703-score" class="post-score" title="current number of votes">0</div><span id="post-38703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm using tshark for some specific dissectors. I have to modify the function <strong>dissect_data(...)</strong> in packet-data.c. In my scenario, most of the packet must go through this function. My objective is: at the end of this function, I want to clear all data of this packet before going to the next in order to free memory. So, my question is:</p><ul><li>Is it possible to clear all data at the end of this function (<strong>dissect_data</strong>)? if YES, how can I do this?</li><li>Can I free the tree by <strong>proto_tree_free(proto_tree *tree)</strong> after processing each packet?</li><li>Is it possible to use some functions like: <strong>epan_cleanup</strong>();<strong>packet_cleanup</strong>();<strong>cleanup_dissection</strong>();</li></ul><p>Here is the function dissect_data(...)</p><pre><code>static void
dissect_data(tvbuff_t *tvb, packet_info *pinfo _U_ , proto_tree *tree)
{
    gint bytes;

        bytes = tvb_length_remaining(tvb, 0);
        if (bytes &gt; 0) {
            tvbuff_t   *data_tvb;
            proto_item *ti;
            proto_tree *data_tree;

            // This is my modification. The output tvb is the same, nothing change.
            tvb = decode_sonnh(tvb,pinfo,tree);

            if (new_pane) {
                guint8 *real_data = (guint8 *)tvb_memdup(tvb, 0, bytes);
                data_tvb = tvb_new_child_real_data(tvb,real_data,bytes,bytes);
                tvb_set_free_cb(data_tvb, g_free);
                add_new_data_source(pinfo, data_tvb, &quot;Not dissected data bytes&quot;);
            } else {
                data_tvb = tvb;
            }
            ti = proto_tree_add_protocol_format(tree, proto_data, tvb,
                0,
                bytes, &quot;Data (%d byte%s)&quot;, bytes,
                plurality(bytes, &quot;&quot;, &quot;s&quot;));
            data_tree = proto_item_add_subtree(ti, ett_data);

            proto_tree_add_item(data_tree, hf_data_data, data_tvb, 0, bytes, ENC_NA);

            if (show_as_text) {
                proto_tree_add_item(data_tree, hf_data_text, data_tvb, 0, bytes, ENC_ASCII|ENC_NA);
            }

            if(generate_md5_hash) {
                const guint8 *cp;
                md5_state_t   md_ctx;
                md5_byte_t    digest[16];
                const gchar  *digest_string;

                cp = tvb_get_ptr(tvb, 0, bytes);

                md5_init(&amp;md_ctx);
                md5_append(&amp;md_ctx, cp, bytes);
                md5_finish(&amp;md_ctx, digest);

                digest_string = bytestring_to_str(digest, 16, &#39;\0&#39;);
                ti = proto_tree_add_string(data_tree, hf_data_md5_hash, tvb, 0, 0, digest_string);
                PROTO_ITEM_SET_GENERATED(ti);
            }

            ti = proto_tree_add_int(data_tree, hf_data_len, data_tvb, 0, 0, bytes);
            PROTO_ITEM_SET_GENERATED (ti);
        }

}</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '14, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Dec '14, 15:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-38703" class="comments-container"><span id="38720"></span><div id="comment-38720" class="comment"><div id="post-38720-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I have to modify the function dissect_data(...) in packet-data.c. In my scenario, most of the packet must go through this function.</p></blockquote><p>Why must it go through that function? <code>dissect_data()</code> is what's used when the data being dissected is of an unknown protocol or is raw data (such as that transported by "read" and "write" requests in remote file system protocols such as SMB, NFS, or AFP). If you're trying to dissect the data, it's <em>not</em> of an unknown protocol, it's of whatever protocol you're trying to dissect - hacking <code>dissect_data()</code> to call another dissector is <em>always</em> the wrong answer, you should be hacking whatever's calling <code>dissect_data()</code> so that it calls your dissector instead.</p></div><div id="comment-38720-info" class="comment-info"><span class="comment-age">(26 Dec '14, 17:00)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="38723"></span><div id="comment-38723" class="comment"><div id="post-38723-score" class="comment-score"></div><div class="comment-text"><p>Hi Harris, the data stream I received from the network is unknown protocol. After my decode function, it becomes the data of sccp. I know It should be better to create a new dissector to decode so that it can be recognized as sccp data and should not go through dissect_data(...) function as described in the method [1]:</p><ul><li>[1] Expected: data stream -&gt; my dissector to decode -&gt; sccp -&gt; ...</li><li>[2] In fact: data stream -&gt; [unknown protocol] packet-data -&gt; my dissector to decode -&gt; sccp -&gt; ...</li></ul><p>But I choose [2] because I don't know how to get the data stream before it goes to dissect_data(...) in the source code. So, I have to use the data in dissect_data(...) of packet-data.c as as described in the method [2].</p></div><div id="comment-38723-info" class="comment-info"><span class="comment-age">(26 Dec '14, 17:39)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="38724"></span><div id="comment-38724" class="comment"><div id="post-38724-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Hi Harris, the data stream I received from the network is unknown protocol. After my decode function, it becomes the data of sccp.</p></blockquote><p>The data stream you receive from the network is for <em>some</em> known protocol, otherwise you wouldn't have a decode function to apply to it!</p><blockquote><p>But I choose [2] because I don't know how to get the data stream before it goes to dissect_data(...) in the source code.</p></blockquote><p>In what protocol is your data stream encapsulated? TCP? IP? Ethernet? If you read a capture file into Wireshark <em>without</em> your decode function, presumably, in the "packet details" pane, there will be <em>some</em> protocol that appears before it. <em>That's</em> the place where <code>dissect_data()</code> gets called.</p></div><div id="comment-38724-info" class="comment-info"><span class="comment-age">(26 Dec '14, 18:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="38725"></span><div id="comment-38725" class="comment"><div id="post-38725-score" class="comment-score"></div><div class="comment-text"><p>Hi Harris. The protocol before it is UDP . <a href="https://www.fshare.vn/file/STJVHL7XSZ9Y">Here</a> is the pcap file. Thanks for suggestion. I 'll try to rewrite the dissector.</p></div><div id="comment-38725-info" class="comment-info"><span class="comment-age">(26 Dec '14, 18:22)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div></div><div id="comment-tools-38703" class="comment-tools"></div><div class="clear"></div><div id="comment-38703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38757"></span>

<div id="answer-container-38757" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38757-score" class="post-score" title="current number of votes">2</div><span id="post-38757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hoangsonk49 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to either:</p><ol><li>have your dissector register in the "udp" dissector table, with <code>dissector_add_uint()</code>, for the UDP ports it uses, if it uses the same UDP ports all the time;</li><li>have your dissector have a preference to specify the UDP ports, and have it register in the "udp" dissector table using those port numbers;</li><li>have your dissector register in the "udp" dissector table with <code>dissector_add_for_decode_as()</code>, so that you can use the "decode as" mechanisms to specify that a particular UDP conversation should be dissected using your protocol;</li><li>if your protocol's packets have some data pattern at the beginning if the protocol's packet that makes it possible to guess what packets are packets with that protocol, make your dissector a "heuristic" dissector and register it in the "udp" heuristic dissector list with <code>heur_dissector_add()</code>.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '14, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Dec '14, 02:16</strong> </span></p></div></div><div id="comments-container-38757" class="comments-container"></div><div id="comment-tools-38757" class="comment-tools"></div><div class="clear"></div><div id="comment-38757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38708"></span>

<div id="answer-container-38708" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38708-score" class="post-score" title="current number of votes">0</div><span id="post-38708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No you cannot, because the dissection engine memory is owned by the dissection engine, not you dissector. The engine knows when memory can be freed, or not, and does so when appropriate. There have been some serious work in this area with current versions of Wireshark, so this might relieve you situation.</p><p>If you are looking at the out-of-memory problems you can encounter when having a long capture, or large file, there are other ways to address this. The root cause is that Wireshark accumulates 'state' from the network traffic it sees. This allows Wireshark to do all the amazing things it does. On the downside, this state data cannot be freed until the capture file is closed.</p><p>So, either capture using dumpcap for long term captures, or use editcap to split your large capture file in order for it to be loaded. But these are only general recommendation. There could be more specific suggestions possible for your particular situation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Dec '14, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-38708" class="comments-container"><span id="38712"></span><div id="comment-38712" class="comment"><div id="post-38712-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap, I split file by using :</p><p><strong>tshark -i 6 -P -w logs/call_log.pcap -b filesize:655350</strong></p><p>In another situation, I dissected the CAMEL packet successfully without any problem of memory.In the current situation,the packet is not a standard so it must be decoded before going through SCCP dissector to be output as CAMEL standard.If CAMEL packet has no problem of memory,so I think there is something wrong in my decode function which are related to the memory allocation. It increases about 1.5% of 32GB in 10 minutes until reach 95% before Stop. Here is the decode function:</p><pre><code>decode_sonnh(tvbuff_t *tvb, packet_info *pinfo _U_ , proto_tree *tree)
{
        tvbuff_t *tvb_sonnh;
        tvbuff_t *tvb_tmp;
        ...    
        if (...)
        {    
             ...    
            guint8 sccp_sonnh[1000];
            guint8 sccp_sonnh_tmp[1000];
            guint8 real_data_sonnh[1000];

            for(i=0;i&lt;bytes;i++)
            {
            value = tvb_get_guint8(tvb, i);
                value1= tvb_get_guint8(tvb, i+1);

                if(...)
                {
                    nStart = ...
                    break;
                }
            }

            if(...)
            {       
                ...
                tvb_tmp = tvb_new_subset_remaining(tvb, nStart);                
                ...
                bytes = tvb_length_remaining(tvb_tmp,0);
                real_data_sonnh[0]=...;
                real_data_sonnh[1]=...;
                real_data_sonnh[2]=...;
                real_data_sonnh[3]=... + nSccp_Called_Length;
                real_data_sonnh[4]=real_data_sonnh[3] + nSccp_Calling_Length;
                for(...)
                {
                    real_data_sonnh[5+i]=sccp_sonnh[i];
                }
                    real_data_sonnh[5+nSccp_length]=...;

                for(...)
                {
                    real_data_sonnh[6+nSccp_length+i]=tvb_get_guint8(tvb_tmp, i);
                }
                    tvb_sonnh = tvb_new_real_data(&amp;real_data_sonnh,bytes+nSccp_length+6,bytes+nSccp_length+6); 
                    dissect_sccp(tvb_sonnh,pinfo,tree ); // Wireshark takes care this dissection.Result is CAMEL packet
                    if(tvb_sonnh)
                    {
                        tvb_free(tvb_sonnh);
                        tvb_sonnh = NULL;
                    }
                    ...

            }
            else
            {
                ...
            }
        }
        else
        {
            ...
        }
     }</code></pre><p>is there any problem with the memory allocation? Please correct me if I did something wrong. Thank you.</p></div><div id="comment-38712-info" class="comment-info"><span class="comment-age">(25 Dec '14, 18:53)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="38713"></span><div id="comment-38713" class="comment"><div id="post-38713-score" class="comment-score"></div><div class="comment-text"><p>It could be related to the SCCP dissector keeping state information. If you are using the 1.99 branch, you can have a look at the -b switch, as described here: <a href="https://blog.wireshark.org/2014/07/to-infinity-and-beyond-capturing-forever-with-tshark/">https://blog.wireshark.org/2014/07/to-infinity-and-beyond-capturing-forever-with-tshark/</a></p></div><div id="comment-38713-info" class="comment-info"><span class="comment-age">(26 Dec '14, 00:50)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="38714"></span><div id="comment-38714" class="comment"><div id="post-38714-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, I'm using the -b switch as mentioned at the top of the comment</p><blockquote><p>tshark -i 6 -P -w logs/call_log.pcap -b filesize:655350</p></blockquote></div><div id="comment-38714-info" class="comment-info"><span class="comment-age">(26 Dec '14, 01:27)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div></div><div id="comment-tools-38708" class="comment-tools"></div><div class="clear"></div><div id="comment-38708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

