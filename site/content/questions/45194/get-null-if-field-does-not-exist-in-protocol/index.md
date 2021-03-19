+++
type = "question"
title = "get NULL if field does not exist in protocol"
description = '''Hello! I have no idea how to solve one problem:  with the help of dumpcap I capture pcap file after that I parse pcap file with tshark  some frames are muti-chunk. For example mapping of the frame is the following: SCTP -&amp;gt; MTP3 -&amp;gt; SCCP -&amp;gt; TCAP -&amp;gt; GSM_MAP -&amp;gt; GSM_SMS -&amp;gt; SCTP -&amp;gt; MT...'''
date = "2015-08-18T04:17:00Z"
lastmod = "2015-08-21T05:58:00Z"
weight = 45194
keywords = [ "lua", "ss7", "gsm_map" ]
aliases = [ "/questions/45194" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [get NULL if field does not exist in protocol](/questions/45194/get-null-if-field-does-not-exist-in-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45194-score" class="post-score" title="current number of votes">0</div><span id="post-45194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I have no idea how to solve one problem:</p><ol><li>with the help of dumpcap I capture pcap file</li><li>after that I parse pcap file with tshark</li><li><p>some frames are muti-chunk. For example mapping of the frame is the following:</p><p><code>SCTP -&gt; MTP3 -&gt; SCCP -&gt; TCAP -&gt; GSM_MAP -&gt; GSM_SMS -&gt;</code></p><p><code>SCTP -&gt; MTP3 -&gt; SCCP -&gt; TCAP -&gt; GSM_MAP -&gt;</code></p><p><code>SCTP -&gt; MTP3 -&gt; SCCP -&gt; TCAP -&gt; GSM_MAP -&gt; GSM_SMS -&gt;</code></p><p><code>SCTP -&gt; MTP3 -&gt; SCCP -&gt; TCAP -&gt; GSM_MAP -&gt; GSM_SMS</code></p></li></ol><p>And with the help of lua script I devide multi-chunk in separate strings</p><p>Code of LUA script:</p><hr /><pre><code>local logfile = &quot;/en_&quot;..os.date(&quot;%Y%m%d%H%M%S&quot;)..&quot;.lua&quot;
io.output(logfile)

local frame_time = Field.new(&quot;frame.time&quot;)
local frame_protocols = Field.new(&quot;frame.protocols&quot;)
local gsm_map_tbcd_digits = Field.new(&quot;gsm_map.tbcd_digits&quot;)

local gsm_map_cap = Listener.new(nil,&quot;gsm_map&quot;)

function gsm_map_cap.packet(pinfo,tvb)

    local Mas_frame_time = frame_time()
    XMas_frame_time = string.gsub(tostring(Mas_frame_time),&quot;  &quot;,&quot; &quot;)
    local Mas_frame_protocols = frame_protocols()
    local Mas_gsm_map_tbcd_digits = {gsm_map_tbcd_digits()}
    p=&quot;(%a+) (%d+), (%d+) (%d+):(%d+):(%d+).(%d+) (%a+)&quot;
    MON={Jan=1,Feb=2,Mar=3,Apr=4,May=5,Jun=6,Jul=7,Aug=8,Sep=9,Oct=10,Nov=11,Dec=12}

    Max_count = 0
    count = 0
    for k,v in ipairs(Mas_gsm_map_tbcd_digits) do
        count = count + 1
    end

    for i=1,Max_count do
        xmonth,xday,xyear,xhour,xmin,xsec,xmlsec,xtz=tostring(XMas_frame_time):match(p)
        month=MON[xmonth]
        local convertedTimestamp = os.date(&quot;%Y-%m-%d %H:%M:%S&quot;,os.time({year = xyear, month = month, day = xday, hour = xhour, min = xmin, sec = xsec}))
        io.write(tostring(convertedTimestamp) .. &quot;\t&quot; ..  tostring(Mas_frame_protocols) .. &quot;\t&quot; .. tostring(Mas_gsm_map_tbcd_digits[i]) .. &quot;\n&quot;)
        end
    end

end</code></pre><hr /><p>But the problem is that in one multi-chunk frame one field (<code>gsm_map.tbcd_digits</code>) could exit in one <code>GSM_MAP</code> and in another <code>GSM_MAP</code> in the same frame this field does not exist.</p><p>Somebody may be knows how to write listener in LUA to get NULL for the field even if this field does not exist in one of the protocol in multi-chunk frame?</p><p>As the result a want to have from lua the following array for field “ <code>gsm_map.tbcd_digits</code> “:</p><pre><code>123123123123123123

456456456456456456

NUL

678768678678678678</code></pre><p>But now a have only following:</p><pre><code>123123123123123123

456456456456456456

678768678678678678</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-ss7" rel="tag" title="see questions tagged &#39;ss7&#39;">ss7</span> <span class="post-tag tag-link-gsm_map" rel="tag" title="see questions tagged &#39;gsm_map&#39;">gsm_map</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '15, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/2d7d6eacf9c502b9188b233cb3e1d8ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="domeno&#39;s gravatar image" /><p><span>domeno</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="domeno has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Aug '15, 04:49</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-45194" class="comments-container"></div><div id="comment-tools-45194" class="comment-tools"></div><div class="clear"></div><div id="comment-45194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45255"></span>

<div id="answer-container-45255" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45255-score" class="post-score" title="current number of votes">1</div><span id="post-45255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="domeno has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try something like this - this doesn't do your whole thing, but should give you the idea:</p><pre><code>-- creates a Proto object, but doesn&#39;t register it yet
local proxy = Proto(&quot;tcap_proxy&quot;,&quot;TCAP-Proxy Fake Protocol&quot;)

-- these protofields are only used for debugging this thing
local total_tbcd_pf = ProtoField.uint16(&quot;tcap_proxy.total_tbcd&quot;,
                                        &quot;Number of TBCD entries created (real and NULL)&quot;)
local real_tbcd_pf  = ProtoField.uint16(&quot;tcap_proxy.real_tbcd&quot;, 
                                        &quot;Number of real TBCD entries created&quot;)
local null_tbcd_pf  = ProtoField.uint16(&quot;tcap_proxy.null_tbcd&quot;, 
                                        &quot;Number of null TBCD entries created&quot;)
proxy.fields = { total_tbcd_pf, real_tbcd_pf, null_tbcd_pf }

-- this is the field we&#39;re going to keep track of
local tbcd_digits_field = Field.new(&quot;gsm_map.tbcd_digits&quot;)

-- this will be the tcap dissector, once we get it later
local tcap_dissector

-- this holds all of counts, in subtables per packet number
local packets = {}

function proxy.dissector(tvbuf,pinfo,root)

    if not pinfo.visited then
        -- first time for this packet, but might not be the first time we&#39;ve
        -- been invoked in this packet; let&#39;s find out
        local counts = packets[pinfo.number]

        if not counts then
            -- ok, it&#39;s the first time we&#39;ve been invoked for this packet, ever.
            -- so create a subtable for this packet&#39;s tbcd_digit counts
            counts = { [&quot;number_real_entries&quot;] = 0 }
            packets[pinfo.number] = counts
        end

        local current_count = #counts

        -- for debugging, we&#39;re going to add our proxy protocol to the tree
        local tree = root:add(proxy, tvbuf:range(0,pktlen))
        tree:add(total_tbcd_pf, current_count):set_generated()
        tree:add(real_tbcd_pf, counts.number_real_entries):set_generated()
        tree:add(null_tbcd_pf, current_count - counts.number_real_entries):set_generated()

        -- call the TCAP dissector
        tcap_dissector:call(tvbuf,pinfo,root)

        local num_fields = { tbcd_digits_field() }

        if #num_fields &gt; counts.number_real_entries then
            -- we got a new one; it must be the last one in the num_fields table
            counts[current_count + 1] = num_fields[#num_fields].value
            counts.number_real_entries = counts.number_real_entries + 1
        else
            -- no tbcd digits, add a &lt;NONE&gt; entry
            counts[current_count + 1] = &quot;&lt;NONE&gt;&quot;
        end
    else
        -- we&#39;ve processed this whole packet before; just show the debug info
        -- of the counts and invoke the TCAP dissector
        local counts = packets[pinfo.number]

        -- for debugging, we&#39;re going to add our proxy protocol to the tree
        local tree = root:add(proxy, tvbuf:range(0,pktlen))
        tree:add(total_tbcd_pf, #counts):set_generated()
        tree:add(real_tbcd_pf, counts.number_real_entries):set_generated()
        tree:add(null_tbcd_pf, #counts - counts.number_real_entries):set_generated()

        -- call the TCAP dissector
        tcap_dissector:call(tvbuf,pinfo,root)
    end

end

-- we&#39;re intercepting SSN range 6-9 for GSM MAP
local sccp_tbl = DissectorTable.get(&quot;sccp.ssn&quot;)
-- get the TCAP dissector
tcap_dissector = sccp_tbl:get_dissector(6)
-- replace it with our proxy dissector, for the 6-9 range
sccp_tbl:set(&quot;6-9&quot;, proxy)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '15, 20:19</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-45255" class="comments-container"><span id="45286"></span><div id="comment-45286" class="comment"><div id="post-45286-score" class="comment-score"></div><div class="comment-text"><p>Hadriel,</p><p>Could you please explain for what is calling "tcap_dissector" inside of "proxy.dissector" (artificial dissector for uor needs)?</p><p>Thanks for help!</p></div><div id="comment-45286-info" class="comment-info"><span class="comment-age">(20 Aug '15, 23:04)</span> <span class="comment-user userinfo">domeno</span></div></div><span id="45295"></span><div id="comment-45295" class="comment"><div id="post-45295-score" class="comment-score"></div><div class="comment-text"><p>If you look at the bottom of the script, you'll see I'm getting the "sccp.ssn" dissector table, and then from within that I'm getting the dissector registered for SCCP SSN number 6, and I'm <em>replacing</em> it with this "proxy" protocol's dissector. (in fact, I'm replacing the whole 6-9 range of SSNs) That dissector I'm <strong>replacing</strong> is the TCAP dissector - the one written in C-code built into wireshark.</p><p>So basically whenever SCCP goes to decode a message of SSN 6-9, instead of invoking TCAP like it would normally do, it invokes our proxy dissector instead. So within the proxy dissector I invoke the original TCAP dissector with the "<code>tcap_dissector:call(tvbuf,pinfo,root)</code>" line.</p><p>The reason I'm doing all that is that I can see if the number of GSM MAP TBCD fields has changed. If it's change, then we've got a new TBCD in the message to save; if it has <strong>not</strong> changed, then I add a "&lt;none&gt;" entry instead.</p><p>The reason I'm replacing the range 6-9 is that those are the GSM MAP SSN numbers, I think.</p></div><div id="comment-45295-info" class="comment-info"><span class="comment-age">(21 Aug '15, 05:58)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-45255" class="comment-tools"></div><div class="clear"></div><div id="comment-45255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45198"></span>

<div id="answer-container-45198" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45198-score" class="post-score" title="current number of votes">1</div><span id="post-45198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the <a href="https://ask.wireshark.org/questions/43543/how-to-iterating-though-a-bundled-ss7-sctp-packet-in-lua">answer to question 43543</a> which is similar.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '15, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-45198" class="comments-container"><span id="45200"></span><div id="comment-45200" class="comment"><div id="post-45200-score" class="comment-score"></div><div class="comment-text"><p>Hadriel, thanks for the reply.</p><p>I am a little bit newbie in LUA and WireShark. That’s why I could not understand how to read every protocol in one frame successively.</p><p>Here is the code of LUA script for my experiments:</p><hr /><p>local logfile = "en_"..os.date("%Y%m%d%H%M%S")..".lua" io.output(logfile)</p><p>local gsm_map_tbcd_digits = Field.new("gsm_map.tbcd_digits") local m3ua = Listener.new(nil,"m3ua")</p><p>function m3ua.packet(pinfo,tvb)</p><p>local Mas_gsm_map_tbcd_digits = {gsm_map_tbcd_digits()} io.write("imsi:" .. tostring( Mas_gsm_map_tbcd_digits[0]) .."\n") io.write("imsi:" .. tostring( Mas_gsm_map_tbcd_digits[1]) .."\n") io.write("imsi:" .. tostring( Mas_gsm_map_tbcd_digits[2]) .."\n") io.write("imsi:" .. tostring( Mas_gsm_map_tbcd_digits[3]) .."\n") io.write("imsi:" .. tostring( Mas_gsm_map_tbcd_digits[4]) .."\n") io.write("imsi:" .. tostring( Mas_gsm_map_tbcd_digits[5]) .."\n") io.write("imsi:" .. tostring( Mas_gsm_map_tbcd_digits[6]) .."\n") io.write("imsi:" .. tostring( Mas_gsm_map_tbcd_digits[7]) .."\n")</p><p>End</p><hr /><p>I run it by the command:</p><p>Tshark –r /file.pcap –X lua_script:devide_imsi.lua</p><p>As far as I can judge I get the whole array of all “gsm_map.tbcd_digits” write in the beginning of the function m3ua.packet. Would you be so kind and explain how to read every protocol in one frame successively? May be you some usefull examples?!</p><p>Thanks for any help!</p></div><div id="comment-45200-info" class="comment-info"><span class="comment-age">(18 Aug '15, 06:43)</span> <span class="comment-user userinfo">domeno</span></div></div><span id="45201"></span><div id="comment-45201" class="comment"><div id="post-45201-score" class="comment-score"></div><div class="comment-text"><p>Oh yeah I keep forgetting the taps aren't invoked until after the whole packet's been dissected. Crap.</p><p>Hmmm... the only way to do it might be to create a "proxy" Lua protocol, remove the "<code>gsm_map</code>" dissector from TCAP's table, register the proxy Lua dissector in its place for TCAP, and within the proxy one invoke the <code>gsm_map</code> dissector and after it returns see what's changed about the fields you're interested in. Yuck.</p><p>Can you share an example capture file for this problem? I might have some time later today to see if I can get the info you want using a Lua script.</p></div><div id="comment-45201-info" class="comment-info"><span class="comment-age">(18 Aug '15, 07:30)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="45237"></span><div id="comment-45237" class="comment"><div id="post-45237-score" class="comment-score"></div><div class="comment-text"><p>Hadriel, thanks for the reply.</p><p>Could you please give me an advise how can i share the pcap file with example for you? Is it possible to send you this file personally as this file has some private information?</p><p>Thanks for any help!</p></div><div id="comment-45237-info" class="comment-info"><span class="comment-age">(19 Aug '15, 05:23)</span> <span class="comment-user userinfo">domeno</span></div></div><span id="45239"></span><div id="comment-45239" class="comment"><div id="post-45239-score" class="comment-score"></div><div class="comment-text"><p>Sure, my email is either <span class="__cf_email__" data-cfemail="721a1316001b171e19320b131a1d1d5c111d1f">[email protected]</span>, or <span class="__cf_email__" data-cfemail="512539347f2334303d7f3930352338343d11363c30383d7f323e3c7f">[email protected]</span></p></div><div id="comment-45239-info" class="comment-info"><span class="comment-age">(19 Aug '15, 05:31)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="45243"></span><div id="comment-45243" class="comment"><div id="post-45243-score" class="comment-score"></div><div class="comment-text"><p>Wiresharks export-pdu function can do SCTP dechunking if that's of any use, this patch in gerrit implements it for tshark but I think the work on it may have stalled <a href="https://code.wireshark.org/review/#/c/5890/">https://code.wireshark.org/review/#/c/5890/</a></p></div><div id="comment-45243-info" class="comment-info"><span class="comment-age">(19 Aug '15, 07:59)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-45198" class="comment-tools"></div><div class="clear"></div><div id="comment-45198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

