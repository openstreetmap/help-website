+++
type = "question"
title = "delay measurement and add tree"
description = '''Hi there, i&#x27;m trying to analyze some custom parts of a frame for benchmarking to check if frames are transported through a system and when transported i try to calculate the delay based on input and output frame timestamps. The Input and Output Frames are identified by a sequence number added to the...'''
date = "2015-11-05T09:31:00Z"
lastmod = "2015-11-05T09:31:00Z"
weight = 47303
keywords = [ "proto_tree_add_item", "wireshark" ]
aliases = [ "/questions/47303" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [delay measurement and add tree](/questions/47303/delay-measurement-and-add-tree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47303-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>i'm trying to analyze some custom parts of a frame for benchmarking to check if frames are transported through a system and when transported i try to calculate the delay based on input and output frame timestamps. The Input and Output Frames are identified by a sequence number added to the testframe. With the LUA Script the sequence number decoding works. Now i want to calculate the Delay by comparing the sequence bumber of input/output. This is also (lookslike) working but i'm unable to add the delay to the ui tree. Looks like it is overwritten. Here's the code:</p><pre><code>    local f = sptlog.fields 
    f.seq = ProtoField.uint32(&quot;sptlog.seq&quot;, &quot;Sequence of Packet&quot;)
    f.sig = ProtoField.uint32(&quot;sptlog.sig&quot;, &quot;Signature&quot;)
    f.tdiff = ProtoField.float(&quot;sptlog.tdiff&quot;, &quot;Time Diff&quot;)

    function sptlog.dissector(buffer, pinfo, tree)

            if buffer:len() &gt; 50 then
                --We first have to find the offset
                SIG_OFF = 0
                diff =0
                for lc = 1,buffer:len()-3,1 do
                    local part = tostring(buffer:range(lc,3))
                    if part == &quot;535443&quot; then
                        SIG_OFF = lc
                        SIG_OFF = SIG_OFF + 3
                        lc = buffer:len()
                    end
                end
                if SIG_OFF ~= 0 then
                    subtree = tree:add(sptlog, buffer(),&quot;STC DATA&quot;)
                    subtree:add(f.sig, buffer:range(SIG_OFF-3,3))
                    seq = buffer:range(SIG_OFF,2):uint()
                    if not pinfo.visited then
                            if not stp_array[seq] then
                                    local timestamp = NSTime(pinfo.abs_ts, select(2,math.modf(pinfo.abs_ts)) * 10^9)
                                    stp_array[seq] = timestamp
                            else
                                local timestamp = NSTime(pinfo.abs_ts, select(2,math.modf(pinfo.abs_ts)) * 10^9)
                                diff = timestamp - stp_array[seq]
                            end
                    end
                    warn (pinfo.abs_ts)
                    warn (diff)
                    warn (&quot;--------&quot;)
                    subtree:add(f.seq, buffer:range(SIG_OFF,2)) 
                    subtree:add(f.tdiff,diff):set_generated()

                end

            end</code></pre><p>The subtree:add(f.tdiff,diff):set_generated() is not working or gets overwritten. Looks like the script parses two packets in the testcapture five times..</p><p>Any idea? Thanks!</p><p>TIA</p><p>Thomas</p></div><div id="question-tags" class="tags-container tags">proto_tree_add_item wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '15, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/b06e5eb073e87534777ed9e71b853879?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tsillaber&#39;s gravatar image" /><p>tsillaber<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tsillaber has no accepted answers">0%</span></p></div></div><div id="comments-container-47303" class="comments-container"></div><div id="comment-tools-47303" class="comment-tools"></div><div class="clear"></div><div id="comment-47303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

