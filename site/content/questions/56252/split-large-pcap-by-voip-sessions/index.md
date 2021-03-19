+++
type = "question"
title = "Split large pcap by VoIP sessions"
description = '''Hi. I&#x27;ve got really large dump with plenty of VoIP sessions (over RTP). I wan&#x27;t to split it into smaller files, but not by time or by size. I want to store each call-session into separate file. Is it possible with Wireshark, tshark or some other tools? I&#x27;ve tried to use the Lua script from examples:...'''
date = "2016-10-09T04:40:00Z"
lastmod = "2016-10-09T14:21:00Z"
weight = 56252
keywords = [ "pcap", "voip" ]
aliases = [ "/questions/56252" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Split large pcap by VoIP sessions](/questions/56252/split-large-pcap-by-voip-sessions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56252-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I've got really large dump with plenty of VoIP sessions (over RTP). I wan't to split it into smaller files, but not by time or by size. I want to store each call-session into separate file. Is it possible with Wireshark, tshark or some other tools? I've tried to use the Lua script from examples: <a href="https://wiki.wireshark.org/Lua/Examples#Dump_VoIP_calls_into_separate_files">https://wiki.wireshark.org/Lua/Examples#Dump_VoIP_calls_into_separate_files</a> But I'm not sure if it really works: nothing happens after script execution...</p></div><div id="question-tags" class="tags-container tags">pcap voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '16, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/9d8e7bdd418d0b727f76b47e655bc465?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trixter&#39;s gravatar image" /><p>trixter<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trixter has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '16, 04:43</p></div></div><div id="comments-container-56252" class="comments-container"><span id="56259"></span><div id="comment-56259" class="comment"><div id="post-56259-score" class="comment-score"></div><div class="comment-text"><p>The Lua script you refer to says</p><pre><code>require &quot;rex_pcre&quot;
require &quot;luasql.mysql&quot;</code></pre><p>so to work, it needs a library processing posix-compliant regular expressions and a library allowing to interface a database (both seem an overkill to me but that's another story).</p><p>During runtime, the script creates a separate capture file for each VoIP call initiated using SIP and dumps to it all packets which belong to that call, based on the RTP and udptl (t38) dissectors' ability to identify the packet of a signalling protocol which contained the command setting up that particular RTP or udptl stream.</p><p>So what surprises me is that you say it does nothing at all, it should at least woe that the libraries are unavailable, or that</p><p>Are your VoIP calls initiated using SIP or using another protocol (because the script doesn't deal with MGCP, H.323, or H.248/MEGACO)?</p><p>Is Lua enabled in your Wireshark setup?</p><p>If it is, does Wireshark complain about anything wrong about Lua?</p><p>If you run tshark, can you see the <code>Starting voip.lua script.</code> line in its output?</p><p>Does the user under which you run Wireshark enough privileges to write into the destination directory?</p></div><div id="comment-56259-info" class="comment-info"><span class="comment-age">(09 Oct '16, 07:08)</span> sindy</div></div><span id="56260"></span><div id="comment-56260" class="comment"><div id="post-56260-score" class="comment-score"></div><div class="comment-text"><p>OK, I've installed pcre and luasql dependencies, now I'm getting: "Lua: Error During execution of dialog callback: [string "-- voip.lua..."]:11: attempt to index global 'luasql' (a nil value)" when trying to execute this script in Wireshark.</p></div><div id="comment-56260-info" class="comment-info"><span class="comment-age">(09 Oct '16, 07:36)</span> trixter</div></div><span id="56261"></span><div id="comment-56261" class="comment"><div id="post-56261-score" class="comment-score"></div><div class="comment-text"><p>Have you created a database <code>voiper</code> accessible using username <code>voiper</code> and password <code>password</code> in your MySQL before running the script?</p><p>After reading the script a bit more carefully, the use of an SQL database still seems to me an overkill as it works with just a single table of few columns so Lua tables (one per column), but I'd recommend to first pushstart it as it is and then eventually get rid of the SQL.</p><p>Besides, it also seems to me that the regexp is required only to extract a proprietary header <code>x-inin-crn</code> from the SIP messages, so it should be possible to leave it out completely.</p><p>And there is also <code>os.clock()</code> used to check whether a packet is still worth handling, so maybe the intention was to use the script only during live capture. Since you seem to be parsing existing files, you should skip this part as well.</p></div><div id="comment-56261-info" class="comment-info"><span class="comment-age">(09 Oct '16, 07:53)</span> sindy</div></div><span id="56262"></span><div id="comment-56262" class="comment"><div id="post-56262-score" class="comment-score"></div><div class="comment-text"><p>Well, looks like dead end for me, because I'm not familiar with Lua in any way and can't make even small changes to this script - it's a blackbox to me :(</p></div><div id="comment-56262-info" class="comment-info"><span class="comment-age">(09 Oct '16, 08:03)</span> trixter</div></div><span id="56263"></span><div id="comment-56263" class="comment"><div id="post-56263-score" class="comment-score"></div><div class="comment-text"><p>The alternative way would be to use MATE, but I assume it would mean just another hue of black to you, and although there is less to learn, there is also less to achieve - namely, MATE won't save the calls to files.</p><p>However, what is the ultimate goal of the exercise? 5000 files, each containing a single call, is also nothing convenient for manual search-through?</p></div><div id="comment-56263-info" class="comment-info"><span class="comment-age">(09 Oct '16, 08:10)</span> sindy</div></div><span id="56264"></span><div id="comment-56264" class="comment not_top_scorer"><div id="post-56264-score" class="comment-score"></div><div class="comment-text"><p>It's just for the sake of convenience: I've got pretty powerful computer, but still opening such a huge file and manipulating with it is a true pain. Also I want to load some sessions to external software for another kinds of processing, but I have to be sure that each file contains a separate session: not just pieces of some sessions split by time or size.</p></div><div id="comment-56264-info" class="comment-info"><span class="comment-age">(09 Oct '16, 08:14)</span> trixter</div></div><span id="56265"></span><div id="comment-56265" class="comment not_top_scorer"><div id="post-56265-score" class="comment-score"></div><div class="comment-text"><p>If you have ever programmed anything, Lua is not that complex to learn, and the business logic is quite simple:</p><ul><li><p>register your tap to get all SIP, RTP and udptl packets</p></li><li><p>create a new output file with each new SIP Call-ID value you extract from an incoming SIP INVITE packet with no To-tag, and maintain a table mapping the Call-ID values to file names</p></li><li><p>copy each SIP packet bearing that Call-ID to the corresponding file, and if it contains an SDP, create a row in a table <code>frame2callid</code> where the value is the Call-ID or the file handle associated to it and the index is the frame number</p></li><li><p>for each RTP (or udptl) packet, use the <code>rt.setup-frame</code> value as an index to the <code>frame2callid</code> table to learn where (to which file) to copy it (and ignore RTP packets which don't have that value).</p></li><li><p>at the end of the capture, close all output files.</p></li></ul><p>This way you'll save all calls whose initial INVITE is present in that capture; calls which had already been running when the capture started will be ignored. So you'll get just the beginning of calls spanning multiple source files.</p><p>Another limitation is that if the telephony engine of Wireshark fails to detect an RTP stream for whatever reason, you miss it too.</p><p>And yet another limitation is that if the traffic contains some complex scenarios like call transfers, or if there is just a B2BUA which decouples the Call-IDs between two branches of the same actual call, you'll have to merge several output files together to get everything related into a single file.</p></div><div id="comment-56265-info" class="comment-info"><span class="comment-age">(09 Oct '16, 08:56)</span> sindy</div></div></div><div id="comment-tools-56252" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-56252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56253"></span>

<div id="answer-container-56253" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56253-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can try do to that with <a href="https://www.tracewrangler.com">TraceWrangler</a>, using an "Extraction" task. By default, that task will split your file into sessions based on socket pairs. My guess is that each of your VoIP session has one specific socket pair which is different from all others.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '16, 04:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-56253" class="comments-container"><span id="56255"></span><div id="comment-56255" class="comment"><div id="post-56255-score" class="comment-score"></div><div class="comment-text"><p>I've tried it on a sample small dump with 2 RTP sessions, but it "extracted" dozens of files... How do I filter only VoIP traffic for extraction?</p></div><div id="comment-56255-info" class="comment-info"><span class="comment-age">(09 Oct '16, 05:43)</span> trixter</div></div><span id="56256"></span><div id="comment-56256" class="comment"><div id="post-56256-score" class="comment-score"></div><div class="comment-text"><p>Nope. Handling FTP is a rose garden as compared to handling VoIP. VoIP uses one protocol (set) to organize calls, and another protocol to deliver the media. The sockets used by the media are indicated in the application layer of the control/signalling protocol, so TraceWrangler would have to parse the control protocol to control handling of other protocols dynamically.</p></div><div id="comment-56256-info" class="comment-info"><span class="comment-age">(09 Oct '16, 05:44)</span> sindy</div></div><span id="56257"></span><div id="comment-56257" class="comment"><div id="post-56257-score" class="comment-score"></div><div class="comment-text"><p>Okay, I'm not that familiar with VoIP captures I have to admit. In this case Tracewrangler won't be of much help, as it doesn't parse VoIP protocols at this time.</p></div><div id="comment-56257-info" class="comment-info"><span class="comment-age">(09 Oct '16, 05:47)</span> Jasper ♦♦</div></div><span id="56258"></span><div id="comment-56258" class="comment"><div id="post-56258-score" class="comment-score"></div><div class="comment-text"><p>OK, got it. So is there any other solution? Maybe I can use some scripting like Pyshark? I've already extracted all sessions as list (CSV) using Wireshark capabilities (~5k sessions). It contains: "Source Address","Source Port","Destination Address","Destination Port","SSRC" and some other fields. Is it possible now to extract correspondent RTP streams line-by-line to separate pcap-files?</p></div><div id="comment-56258-info" class="comment-info"><span class="comment-age">(09 Oct '16, 05:56)</span> trixter</div></div></div><div id="comment-tools-56253" class="comment-tools"></div><div class="clear"></div><div id="comment-56253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56269"></span>

<div id="answer-container-56269" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56269-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've never collected enough motivation to write a Lua listener, and now I know why.</p><p>If you are 150 % sure that the SIP part of your VoIP traffic uses solely non-fragmented UDP packets as transport, the Lua code below is what you asked for, except that I haven't tested it on captures containing RTCP or T.38 packets.</p><p>Fragmentation of SIP packets as well as use of TCP as SIP transport renders it unusable, because the way it is written, the listener always receives only the last fragment of reassembled SIP PDUs, regardless whether they have been reassembled from IP fragments or TCP segments (or both), because the SIP dissector is invoked only when processing the reassembled transport layer.</p><p>To fix this, it would be necessary to send to the listener all the IP fragments and TCP segments, and the listener would have to remember them until they would become reassembled and then, depending on whether the result of the reassembly contained a valid SIP PDU or not, either save them to the output file (possibly creating weird negative timestamp deltas if an RTP packet would squeeze between two fragments of a SIP PDU) or just drop them.</p><p>Also, bear in mind that the <code>Dumper.new</code> method <strong>appends</strong> data to existing files, so you have to clean up the output directory before opening the same source capture another time.</p><pre><code>-- the output directory may be &quot;hardcoded&quot; this simple way,
-- but if you use command line (tshark) and thus you can set
-- environment variables, use
-- local outputdir = os.getenv(&quot;my_output_path&quot;)
-- as a way to fetch the path from an environment
-- variable &quot;my_output_path&quot; instead

local outputdir = &quot;c:/Users/your_login/Documents&quot;

-- declare the Lua table for file handles
local files = {}

-- declare the Lua table of frames containing SDPs
local sdp_frames = {}

-- prepare the field extractors for the individual protocol types which we are tapping
local frame_number_f = Field.new(&quot;frame.number&quot;)

local rtp_setup_frame_f = Field.new(&quot;rtp.setup-frame&quot;)

local t38_setup_frame_f = Field.new(&quot;t38.setup-frame&quot;)

local rtcp_setup_frame_f = Field.new(&quot;rtcp.setup-frame&quot;)

local sip_callid_f = Field.new(&quot;sip.Call-ID&quot;)
local sip_method_f = Field.new(&quot;sip.Method&quot;)
local sip_to_tag_f = Field.new(&quot;sip.to.tag&quot;)

local sdp_version_f = Field.new(&quot;sdp.version&quot;)

-- create and register the listener
local tap = Listener.new(&quot;ip&quot;, &quot;rtp or rtcp or t38 or (sip and !(sip.CSeq.method == REGISTER) and !(sip.CSeq.method == OPTIONS))&quot;)

-- declare the executive body of the tap
function tap.packet(pinfo,tvb,ip)

-- declare a common function handling all media-like packets
  function handle_media(setup_frame)
    -- if a setup frame for this media stream has actually been encountered, save the packet
    if sdp_frames[setup_frame] then
      files[sdp_frames[setup_frame]]:dump_current()
    end
  end

-- attempt to extract all signature values
  local frame_number = frame_number_f().value -- I can do it this because frame.number always exists
  local sip_callid = sip_callid_f()
  local sip_method = sip_method_f()
  local sip_to_tag = sip_to_tag_f()
  local sdp_version = sdp_version_f()
  local rtp_setup_frame = rtp_setup_frame_f()
  local rtcp_setup_frame = rtcp_setup_frame_f()
  local t38_setup_frame = t38_setup_frame_f()

-- handle SIP packets
  if sip_callid then
    sip_callid_v = sip_callid.value

-- check whether the PDU is an initial INVITE, and create a call if it is and if that call doesn&#39;t exist yet
-- because there was an unauthorized initial INVITE before
    sip_method = sip_method_f()
    if sip_method then
      if (sip_method.value == &quot;INVITE&quot; and not(sip_to_tag_f()) and not(files[sip_callid_v])) then
        local f_handle = Dumper.new_for_current( outputdir .. &quot;/&quot; .. tostring(sip_callid) ..&quot;.pcap&quot; )
        files[sip_callid_v] = f_handle
      end
    end

-- check whether the PDU contains an SDP and if so, add the frame to the list
-- of those responsible for media stream establishment
    if files[sip_callid_v] then
      if sdp_version then
        sdp_frames[frame_number] = sip_callid_v
      end
    end

-- finally, if the frame belongs to an existing call, copy it to the output file
    local f_handle = files[sip_callid_v]
    if f_handle then
      f_handle:dump_current()
    end
  end

-- handle &quot;media&quot; packets
  if rtp_setup_frame then
    handle_media(rtp_setup_frame.value)
  end

  if rtcp_setup_frame then
    handle_media(rtcp_setup_frame.value)
  end

  if t38_setup_frame then
    handle_media(t38_setup_frame.value)
  end

end

-- declare the function to print the progress, not actually necessary
function tap.draw()
end

-- declare what to do after the last packet has been processed
function tap.reset()
  -- close all files at once here, which may be way too late if there are hundreds of calls
  -- and so you may run out of your file handle quota
  for call_id,f_handle in pairs(files) do
    f_handle:flush()
    f_handle:close()
  end
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '16, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '16, 14:27</p></div></div><div id="comments-container-56269" class="comments-container"></div><div id="comment-tools-56269" class="comment-tools"></div><div class="clear"></div><div id="comment-56269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

