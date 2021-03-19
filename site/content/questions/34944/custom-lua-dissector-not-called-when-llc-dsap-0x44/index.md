+++
type = "question"
title = "custom lua dissector not called when llc dsap 0x44"
description = '''Hi, When i use customed dissector to parse data field in LLC, I found the dissector not be called. Can anyone help me about how to make it work? thx qos-llc-data-proto = Proto (&quot;qos-llc-data&quot;, &quot;qos test llc data&quot;, &quot;protocol qos test llc data&quot;)  .....  qos-llc-data-proto.fields = { f-llc-u8-type, f-l...'''
date = "2014-07-28T08:20:00Z"
lastmod = "2014-07-28T08:20:00Z"
weight = 34944
keywords = [ "llc", "dsap", "dissector", "lua" ]
aliases = [ "/questions/34944" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [custom lua dissector not called when llc dsap 0x44](/questions/34944/custom-lua-dissector-not-called-when-llc-dsap-0x44)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34944-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When i use customed dissector to parse data field in LLC, I found the dissector not be called. Can anyone help me about how to make it work? thx</p><pre><code>qos-llc-data-proto = Proto (&quot;qos-llc-data&quot;, &quot;qos test llc data&quot;, &quot;protocol qos test llc data&quot;)

.....

qos-llc-data-proto.fields = { f-llc-u8-type, f-llc-u16-sequence, f-llc-u32-tick, f-llc-u8-priority, f-llc-bytes-data }

function qos-llc-data-proto.dissector(buffer,pinfo,tree)
{
...  
}

local my-dsap = 68

local llc-table = DissectorTable.get(&quot;llc.dsap&quot;)

llc-table:add(68, qos-llc-data-proto)</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/1_4.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">llc dsap dissector lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '14, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/7b6f62723a894576f644d5e2f51933e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireshark_xg&#39;s gravatar image" /><p>wireshark_xg<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireshark_xg has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jul '14, 08:51</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-34944" class="comments-container"><span id="34946"></span><div id="comment-34946" class="comment"><div id="post-34946-score" class="comment-score"></div><div class="comment-text"><p>I assume your code example is fake, rather than from the real script code, since it uses illegal variable names. (dashes are illegal in names) But the general concept of the script appears ok.</p><p>Some basic questions:</p><ol><li><p>Do you know that your script is actually being loaded at all? For example if you put a syntactic error in it does wireshark error trying to load it, or if you put a print statement in it does it print when wireshark loads?</p></li><li><p>Is your packet the right kind of packet for that "llc.dsap" table - I don't know anything about LLC packets, but it appears that "llc.dsap" table only gets looked up for specific xDLC packets, for control information types. It looks like your example packet in the capture above is the right type, but I don't know for sure.</p></li><li><p>Can you post the capture file somewhere? Like on cloudshark or someplace public?</p></li></ol></div><div id="comment-34946-info" class="comment-info"><span class="comment-age">(28 Jul '14, 14:59)</span> Hadriel</div></div><span id="34947"></span><div id="comment-34947" class="comment"><div id="post-34947-score" class="comment-score"></div><div class="comment-text"><p>Hi Hadriel, Sorry for not describe it clearly.</p><p>1.Following is detailed code.</p><pre><code>qos_llc_data_proto = Proto (&quot;qos-llc-data&quot;, &quot;qos test llc data&quot;, &quot;protocol qos test llc data&quot;)

local f_llc_u8_type = ProtoField.uint8(&quot;qos-llc-data.type&quot;, &quot;type&quot;, base.DEC)
local f_llc_u16_sequence = ProtoField.uint16(&quot;qos-llc-data.sequence&quot;, &quot;sequence&quot;, base.DEC)
local f_llc_u32_tick = ProtoField.uint32(&quot;qos-llc-data.tick&quot;, &quot;tick&quot;, base.DEC)
local f_llc_u8_priority = ProtoField.uint8(&quot;qos-llc-data.priority&quot;, &quot;priority&quot;, base.DEC)
local f_llc_bytes_data = ProtoField.bytes(&quot;qos-llc-data.bytesData&quot;, &quot;data&quot;, base.DEC)

qos_llc_data_proto.fields = { f_llc_u8_type, f_llc_u16_sequence, f_llc_u32_tick, f_llc_u8_priority, f_llc_bytes_data }
f_proto = DissectorTable.new(&quot;gnunet.proto&quot;, &quot;Gnunet Protocoll&quot;, FT_UINT16, BASE_DEC)

function qos_llc_data_proto.dissector(buffer,pinfo,tree)
    pinfo.cols.protocol:set(&quot;qos-test-llc-data&quot;)

    pinfo.cols.info:set(&quot;qos test llc data&quot;)

    local buffer_len = buffer:len()
    local myProtoTree = tree:add(qos_llc_data_proto, buffer(0, buffer_len), &quot;qos-test-llc-data&quot;)

    buffer:len_asdf()

    local offset = 0
    myProtoTree:add_le(f_llc_u8_type, buffer(offset, 1))
    offset = offset + 1

    myProtoTree:add_le(f_llc_u16_sequence, buffer(offset, 2):uint())
    offset = offset + 2

    myProtoTree:add_le(f_llc_u32_tick, buffer(offset, 4):uint())
    offset = offset + 4

    myProtoTree:add_le(f_llc_u8_priority, buffer(offset, 1))
    offset = offset + 1

    myProtoTree:add_le(f_llc_bytes_data, buffer(offset, (buffer_len - offset)))
end

local my_dsap = 68 
local llc_table = DissectorTable.get(&quot;llc.dsap&quot;)
llc_table:add(68, qos_llc_data_proto)</code></pre><p>2 From picture, you can find size of LLC packet is 1052, so i want to parse its data field as above code. I don't how to add my dissector to it or how to parse it. I already use similar dissector and add it to port of UDP, and it can works well.</p></div><div id="comment-34947-info" class="comment-info"><span class="comment-age">(28 Jul '14, 15:28)</span> wireshark_xg</div></div><span id="34948"></span><div id="comment-34948" class="comment"><div id="post-34948-score" class="comment-score"></div><div class="comment-text"><ol><li>I already checked that llc_table is not nil after it is get from DissectorTable.get("llc.dsap").</li><li>From picture, you can find DSAP field of packet is 0x44.</li></ol></div><div id="comment-34948-info" class="comment-info"><span class="comment-age">(28 Jul '14, 15:31)</span> wireshark_xg</div></div><span id="34949"></span><div id="comment-34949" class="comment"><div id="post-34949-score" class="comment-score"></div><div class="comment-text"><ol><li>I tried add some error in dissector function qos_llc_data_proto.dissector(buffer,pinfo,tree), find the dissector is not loaded. I don't know why?</li></ol></div><div id="comment-34949-info" class="comment-info"><span class="comment-age">(28 Jul '14, 16:30)</span> wireshark_xg</div></div><span id="34970"></span><div id="comment-34970" class="comment"><div id="post-34970-score" class="comment-score"></div><div class="comment-text"><p>What kind of error did you try to introduce in the dissector? The error needs to be a syntactic Lua error, as opposed to just accessing an invalid/non-existent function (for example). Because during load the script is parsed by the Lua interpreter, but the dissector function code isn't actually executed yet until later. So the error needs to be something fundamentally invalid in Lua language. For example, just put the word "foobar" on a line, even outside the dissector function... like at the top of your script.</p></div><div id="comment-34970-info" class="comment-info"><span class="comment-age">(29 Jul '14, 07:30)</span> Hadriel</div></div><span id="34971"></span><div id="comment-34971" class="comment not_top_scorer"><div id="post-34971-score" class="comment-score"></div><div class="comment-text"><p>If the script file itself isn't being loaded, how did you try loading it? Did you put it in the appropriate plugins directory to be auto-loaded, or are you trying to load it using <code>dofile()</code>, or what?</p></div><div id="comment-34971-info" class="comment-info"><span class="comment-age">(29 Jul '14, 07:32)</span> Hadriel</div></div><span id="34979"></span><div id="comment-34979" class="comment not_top_scorer"><div id="post-34979-score" class="comment-score"></div><div class="comment-text"><blockquote><p>it appears that "llc.dsap" table only gets looked up for specific xDLC packets, for control information types</p></blockquote><p>It's used for I and UI frames, rather than S frames or UI frames other than UI frames.</p><blockquote><p>It looks like your example packet in the capture above is the right type</p></blockquote><p>"Control field: I" indicates that it's an I frame, so, yes, it's the right type, at least in Wireshark 1.10 and later (I don't know whether earlier versions supported it only for U frames).</p></div><div id="comment-34979-info" class="comment-info"><span class="comment-age">(29 Jul '14, 13:34)</span> Guy Harris ♦♦</div></div><span id="34980"></span><div id="comment-34980" class="comment not_top_scorer"><div id="post-34980-score" class="comment-score"></div><div class="comment-text"><p>Which version of Wireshark is this?</p></div><div id="comment-34980-info" class="comment-info"><span class="comment-age">(29 Jul '14, 13:34)</span> Guy Harris ♦♦</div></div><span id="35019"></span><div id="comment-35019" class="comment not_top_scorer"><div id="post-35019-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply. If i add some error line outside dissector function, when wireshark is started, there is error reported. But if i just add error line into dissector function, there is no error reported. As you said, dissector function is executed when parse real network data. So it means that my dissector is not executed really. So my question is it how to parse LLC data field in my case.</p></div><div id="comment-35019-info" class="comment-info"><span class="comment-age">(30 Jul '14, 15:48)</span> wireshark_xg</div></div><span id="35023"></span><div id="comment-35023" class="comment not_top_scorer"><div id="post-35023-score" class="comment-score"></div><div class="comment-text"><p>I find the reason why dissector not call. When reading source code of wireshark, i found following code.</p><pre><code>        if (XDLC_IS_INFORMATION(control)) {
                /*
                 * Non-SNAP I or UI frame.
                 * Try the regular LLC subdissector table
                 * with the DSAP.
                 */
               if (!dissector_try_uint(dsap_subdissector_table,
                    dsap, next_tvb, pinfo, tree)) {
                    call_dissector(data_handle, next_tvb,
                        pinfo, tree);
                }
        }

#define XDLC_IS_INFORMATION(control) \
    (((control) &amp; XDLC_I_MASK) == XDLC_I || (control) == (XDLC_UI|XDLC_U))</code></pre><p>From above code, if XDCL is information, then dsap dissector will called. But from ftype of my frame, it is one XDCL_S which means Supervisory frame. So dsap dissector will not call. So the question is how to parse data filed of LLC. I don't how to add my dissector after parse LLC? In the page <a href="http://wiki.wireshark.org/Lua/Dissectors,">http://wiki.wireshark.org/Lua/Dissectors,</a> it gives examples. But which type can be used in my case? thx</p></div><div id="comment-35023-info" class="comment-info"><span class="comment-age">(30 Jul '14, 17:47)</span> wireshark_xg</div></div><span id="35024"></span><div id="comment-35024" class="comment not_top_scorer"><div id="post-35024-score" class="comment-score"></div><div class="comment-text"><p>To quote IEEE Std 802.2-2008 section 5.4.2.2 "Supervisory format commands and responses":</p><blockquote><p>PDUs with the S format shall not contain an information field</p></blockquote><p>Therefore, there is nothing to hand to a dissector - there <strong><em>IS</em></strong> no data field in an S frame! - so we don't call dissectors for S frames.</p></div><div id="comment-35024-info" class="comment-info"><span class="comment-age">(30 Jul '14, 18:00)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-34944" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-34944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

