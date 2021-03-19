+++
type = "question"
title = "how to display s1ap.gTP_TEID as decimal format?"
description = '''how to display gtp-teid as decimal format? s1ap.gTP-TEID: d7e29a65'''
date = "2013-10-16T16:01:00Z"
lastmod = "2013-10-17T07:41:00Z"
weight = 26091
keywords = [ "decimal", "s1ap.gtp_teid" ]
aliases = [ "/questions/26091" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to display s1ap.gTP\_TEID as decimal format?](/questions/26091/how-to-display-s1apgtp_teid-as-decimal-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26091-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to display gtp-teid as decimal format? s1ap.gTP-TEID: d7e29a65</p></div><div id="question-tags" class="tags-container tags">decimal s1ap.gtp_teid</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '13, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/c3313abf7bef27ecc8a7f656c5fe22da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ertsali&#39;s gravatar image" /><p>ertsali<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ertsali has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '13, 03:13</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-26091" class="comments-container"></div><div id="comment-tools-26091" class="comment-tools"></div><div class="clear"></div><div id="comment-26091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26133"></span>

<div id="answer-container-26133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26133-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>how to display gtp-teid as decimal format? gTP-TEID: d7e29a65</p></blockquote><p>for that single value: 3621952101</p><p>In General: By adding a Lua post dissector that takes the original value and adds a new field for the decimal value.</p><p>Here is a <strong>very simple</strong> (but working) sample code, based on the <a href="http://diablohorn.wordpress.com/2010/12/05/dnscat-traffic-post-dissector/">DnsCat Lua post dissector</a></p><p>File: gtp_ext.lua</p><pre><code>-- info
print(&quot;gtp postdissector loaded&quot;)

-- we need these fields from the gtp packets
gtp_teid = Field.new(&quot;gtp.teid&quot;)

-- declare our postdissector
gtp_pd = Proto(&quot;gtp_ext&quot;,&quot;gtp TEID decical converter postdissector&quot;)

-- our fields
gtp_teid_decimal = ProtoField.uint32(&quot;gtp.teid_decimal&quot;,&quot;GTP TEID in decimal format&quot;)
gtp_pd.fields = {gtp_teid_decimal}

-- dissect each packet
function gtp_pd.dissector(buffer,pinfo,tree)
 local gtpteid  = gtp_teid()

 if (gtpteid) then
    subtree = tree:add(gtp_pd,&quot;GTP decimal data&quot;)
    subtree:add(gtp_teid_decimal,tostring(gtpteid))
 end
end -- end dissector function

-- register ourselfs
register_postdissector(gtp_pd)</code></pre><p>Place the file gtp_ext.lua (gtp_ext == extended GTP) in the Wireshark installation directory. Then edit <strong>init.lua</strong>. Add the following line:</p><blockquote><p>dofile(DATA_DIR.."gtp_ext.lua")</p></blockquote><p>Close Wireshark and open it again. Open a GTP pcap and filter for</p><blockquote><p>gtp.teid</p></blockquote><p>All frames with a gtp.teid will have a new field called</p><blockquote><p>gtp.teid_decimal</p></blockquote><p>You can also use the new field in a display filter, like this:</p><blockquote><p>gtp.teid_decimal &gt; 10000000 or gtp.teid_decimal eq 200000</p></blockquote><p>See the following screenshot</p><p><img src="https://osqa-ask.wireshark.org/upfiles/gtp_ext_screenshot_1.png" alt="alt text" /></p><p>Have fun!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '13, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '13, 09:23</p></div></div><div id="comments-container-26133" class="comments-container"><span id="26149"></span><div id="comment-26149" class="comment"><div id="post-26149-score" class="comment-score"></div><div class="comment-text"><p>Thanks.. this is awesome but I would like to decode s1ap.gTP_TEID. Please help to modify the coding based on s1ap.gTP_TEID.</p></div><div id="comment-26149-info" class="comment-info"><span class="comment-age">(17 Oct '13, 15:27)</span> ertsali</div></div><span id="26160"></span><div id="comment-26160" class="comment"><div id="post-26160-score" class="comment-score"></div><div class="comment-text"><p>Basically: Just replace the string 'gtp.teid' in the code with 's1ap.gTP_TEID'. Unfortunately I don't have pcap file with s1ap traffic to test it.</p><p>new code:</p><pre><code>-- info
print(&quot;gTP_TEID postdissector loaded&quot;)

-- we need these fields from the gtp packets
s1ap_gtp_teid = Field.new(&quot;s1ap.gTP_TEID&quot;)

-- declare our postdissector
teid_pd = Proto(&quot;teid_decimal&quot;,&quot;s1ap gTP_TEID decical converter postdissector&quot;)

-- our fields
s1ap_gtp_teid_decimal = ProtoField.uint32(&quot;s1ap.gTP_TEID_decimal&quot;,&quot;S1AP gTP_TEID in decimal&quot;)
teid_pd.fields = {s1ap_gtp_teid_decimal}

-- dissect each packet
function teid_pd.dissector(buffer,pinfo,tree)
 local s1apgtpteid  = s1ap_gtp_teid()

 if (gtpteid) then
    subtree = tree:add(teid_pd,&quot;gTP_TEID decimal data&quot;)
    subtree:add(s1ap_gtp_teid_decimal,tostring(s1apgtpteid))
 end
end -- end dissector function

-- register ourselfs
register_postdissector(teid_pd)</code></pre></div><div id="comment-26160-info" class="comment-info"><span class="comment-age">(18 Oct '13, 03:11)</span> Kurt Knochner ♦</div></div><span id="26208"></span><div id="comment-26208" class="comment"><div id="post-26208-score" class="comment-score"></div><div class="comment-text"><p>Cannot work. Please help and download the log via the link. <a href="https://skydrive.live.com/?cid=2d4afe2cec0bd503&amp;id=2D4AFE2CEC0BD503%21666&amp;action=Share">https://skydrive.live.com/?cid=2d4afe2cec0bd503&amp;id=2D4AFE2CEC0BD503%21666&amp;action=Share</a></p></div><div id="comment-26208-info" class="comment-info"><span class="comment-age">(19 Oct '13, 02:23)</span> ertsali</div></div><span id="26233"></span><div id="comment-26233" class="comment"><div id="post-26233-score" class="comment-score"></div><div class="comment-text"><p>O.K. with s1ap it's not that simple, as there can be several gtp_TEID fields in one frame. So, it's unclear how the post dissector should show them? Just in the same order as they appeared in the original frame, one after the other?</p></div><div id="comment-26233-info" class="comment-info"><span class="comment-age">(21 Oct '13, 03:41)</span> Kurt Knochner ♦</div></div><span id="26272"></span><div id="comment-26272" class="comment"><div id="post-26272-score" class="comment-score"></div><div class="comment-text"><p>I see. Thanks</p></div><div id="comment-26272-info" class="comment-info"><span class="comment-age">(21 Oct '13, 21:19)</span> ertsali</div></div><span id="26273"></span><div id="comment-26273" class="comment not_top_scorer"><div id="post-26273-score" class="comment-score"></div><div class="comment-text"><p>Kind of speaking to Kurt's last question, is there a specific end goal in mind here ertsali? Are you trying to correlate the trace file with MME queries, for example? Easy enough to use the above method to just display all the TEIDs, and if also bound to a procedure code I believe the order should always be predictable as well, unless the vendor is doing something odd like passing separate S1AP commands as data chunks in a single packet.</p><p>There's probably easier ways depending on the end goal though. For example, converting the other way from a vendor's stat file might just be a one-liner script as opposed to breaking out Lua to map Wireshark to the format of a stat or log file.</p></div><div id="comment-26273-info" class="comment-info"><span class="comment-age">(21 Oct '13, 21:25)</span> Quadratic</div></div></div><div id="comment-tools-26133" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-26133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26131"></span>

<div id="answer-container-26131" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26131-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>By changing the code in packet-gtp.c, otherwise you have to bring out your calculator.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '13, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-26131" class="comments-container"></div><div id="comment-tools-26131" class="comment-tools"></div><div class="clear"></div><div id="comment-26131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

