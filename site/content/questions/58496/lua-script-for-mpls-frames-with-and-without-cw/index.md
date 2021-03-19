+++
type = "question"
title = "lua script for mpls frames with AND without cw"
description = '''we have a mix of different mpls frames with and without cw.  if a cw is present, then its value is always 0 - in our implementation we have no cw&#x27;s with a value different from 0. so our question is how we might be able to write a small lua script  to accomplish, that: in the case, that the first fou...'''
date = "2017-01-04T05:59:00Z"
lastmod = "2017-01-08T13:59:00Z"
weight = 58496
keywords = [ "lua", "mpls" ]
aliases = [ "/questions/58496" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [lua script for mpls frames with AND without cw](/questions/58496/lua-script-for-mpls-frames-with-and-without-cw)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58496-score" class="post-score" title="current number of votes">0</div><span id="post-58496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>we have a mix of different mpls frames with and without cw.</p><p>if a cw is present, then its value is always 0 - in our implementation we have no cw's with a value different from 0.</p><p>so our question is how we might be able to write a small lua script to accomplish, that:</p><p>in the case, that the first four bytes of the encapsulated ethernet frame are not all zero, then we assume that they contain the start of the destination mac address ... and hence just simply continue with the dissection.</p><p>if on the other hand the first four bytes of the encapsulated ethernet frame are all zero then we assume to have a control-word and would like to strip it away before we may continue with the dissection of the frame.</p><p>would that be possible ? any hints ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-mpls" rel="tag" title="see questions tagged &#39;mpls&#39;">mpls</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '17, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/742ba5366f391cc1422562fa87e3665b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="x42&#39;s gravatar image" /><p><span>x42</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="x42 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jan '17, 09:28</strong> </span></p></div></div><div id="comments-container-58496" class="comments-container"><span id="58498"></span><div id="comment-58498" class="comment"><div id="post-58498-score" class="comment-score"></div><div class="comment-text"><p>Ugh, MPLS control words are just a pain to get right. Heuristically it's almost impossible to determine definitively (I experimenting with a Wireshark change, not done yet).</p><p>Anyway, your case should be possible, if you can insert yourself as MPLS ethertype dissector, then examine the first octets of the TVB and decide which dissector to call.</p></div><div id="comment-58498-info" class="comment-info"><span class="comment-age">(04 Jan '17, 06:27)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="58565"></span><div id="comment-58565" class="comment"><div id="post-58565-score" class="comment-score"></div><div class="comment-text"><p>we have only a dirty and tedious workaround for the present case, that the cw's can only take on the value 0:</p><p>1) open the mixed trace (mpls packets with and without cw) and apply the lua-script</p><pre><code>local success, dis_eth = pcall(Dissector.get, &quot;eth_withoutfcs&quot;)
if not success or not dis_eth then
  dis_eth = Dissector.get(&quot;eth&quot;)
end

local mpls_table = DissectorTable.get(&quot;mpls.label&quot;)
for label=0,1048575 do
  mpls_table:add(label,dis_eth)
end</code></pre><p>2) apply the display filter <code>eth.dst[0:4]==00:00:00:00</code> and save the displayed frames as capture-with-cw.pcap</p><p>3) apply the complementary display filter <code>!(eth.dst[0:4]==00:00:00:00)</code></p><p>4) open the previously saved capture-with-cw.pcap in a second instance of wireshark (it must be 1.x because the <code>pw_eth_cw</code> dissector is not present in wireshark 2.x <a href="https://ask.wireshark.org/questions/58532/missing-dissector-pw_eth_cw">https://ask.wireshark.org/questions/58532/missing-dissector-pw_eth_cw</a> )</p><p>and apply the lua-script</p><pre><code>dis_eth_cw = Dissector.get(&quot;pw_eth_cw&quot;)
local mpls_table = DissectorTable.get(&quot;mpls.label&quot;)
for label=0,1048575 do
  mpls_table:add(label,dis_eth_cw)
end</code></pre><p>5) analyze the original trace in the two wireshark instances ...</p><p>so yes ... we are hoping very much that your modifications/changes to the mpls-heuristic may be successfull :-)</p></div><div id="comment-58565-info" class="comment-info"><span class="comment-age">(06 Jan '17, 10:21)</span> <span class="comment-user userinfo">x42</span></div></div></div><div id="comment-tools-58496" class="comment-tools"></div><div class="clear"></div><div id="comment-58496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58601"></span>

<div id="answer-container-58601" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58601-score" class="post-score" title="current number of votes">0</div><span id="post-58601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>now, that the missing dissectors <code>pw_eth_cw</code> and <code>pw_eth_nocw</code> have found their way back into the wireshark source-code, we may use the following script to switch between appropriate dissectors as needed:</p><pre><code>info(&quot;MPLS script loaded ...&quot;)

local tap_mpls = Listener.new(&quot;eth&quot;)
local mpls_table = DissectorTable.get(&quot;mpls.label&quot;)

dis_eth_cw = Dissector.get(&quot;pw_eth_cw&quot;)
dis_eth_nocw = Dissector.get(&quot;pw_eth_nocw&quot;)

eth_dst_f = Field.new(&quot;eth.dst&quot;)
mpls_label_f = Field.new(&quot;mpls.label&quot;)

function tap_mpls.packet(pinfo, tvb, eth)

-- as we may or may not have multiple vlan encapsulations
-- we would like to avoid using an explicit offset like e.g. 
-- local cw = tvb(22,4):uint()

  local eth_dst = tostring(eth_dst_f())
  local mpls_label = tostring(mpls_label_f())

-- in our case only cw&#39;s = 0 might be present
-- this makes the heuristic relatively easy

  local dst = tostring(eth.dst)
  if string.find(dst, &quot;00:00:00_00&quot;)==1 or string.find(dst, &quot;00:00:00:00&quot;)==1 then
    debug(&quot;cw==0 found in packet &quot; .. pinfo.number .. &quot; label &quot; .. mpls_label)
    debug(&quot;changing dissector for label &quot; .. mpls_label)

    mpls_table:remove(mpls_label,dis_eth_nocw)
    mpls_table:add(mpls_label,dis_eth_cw)
  end
end

function tap_mpls.reset()
  debug(&quot;reset ... assuming we have no cw&#39;s&quot;)
  mpls_table:remove_all(dis_eth_nocw)
  mpls_table:remove_all(dis_eth_cw)
  for label=0,1048575 do
    mpls_table:add(label,dis_eth_nocw)
  end
end

function tap_mpls.draw()
  debug(&quot;--------------------------------------&quot;)
end</code></pre><p>it would be even better if we knew how to "insert ourself into the mpls ethertype dissector" as suggested, but it's ok ... the script works satisfactory in our network.</p><p>we are now able to analyze different cases in the (very buggy) mpls-implementation of a well-known hardware vendor ;-)</p><p>thanks a lot to you all for your friendly, swift and very competent support and insight into mpls-related problems !</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '17, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/742ba5366f391cc1422562fa87e3665b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="x42&#39;s gravatar image" /><p><span>x42</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="x42 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jan '17, 14:01</strong> </span></p></div></div><div id="comments-container-58601" class="comments-container"></div><div id="comment-tools-58601" class="comment-tools"></div><div class="clear"></div><div id="comment-58601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

