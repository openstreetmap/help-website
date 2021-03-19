+++
type = "question"
title = "Lua: cannot read SNMP request_id field"
description = '''Hello WIRESHARK community! I need your help because i mark time here with a little Lua scripting problem. My aim is to count lost SNMP transactions. Therefore i need to read out the snmp.request_id field to handle requests and responses belonging together. Unfortunately it is not working as it shoul...'''
date = "2011-03-04T01:02:00Z"
lastmod = "2011-03-04T01:02:00Z"
weight = 2660
keywords = [ "lua", "dissector", "tshark" ]
aliases = [ "/questions/2660" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua: cannot read SNMP request\_id field](/questions/2660/lua-cannot-read-snmp-request_id-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2660-score" class="post-score" title="current number of votes">1</div><span id="post-2660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello WIRESHARK community!</p><p>I need your help because i mark time here with a little Lua scripting problem. My aim is to count lost SNMP transactions. Therefore i need to read out the snmp.request_id field to handle requests and responses belonging together. Unfortunately it is not working as it should. Here is my little debugging code example &lt;snmpreqid.lua&gt;:</p><pre><code>snmp_reqID_extr = Field.new(&quot;snmp.request_id&quot;)
snmp = Listener.new(nil,&quot;snmp&quot;);
function snmp.packet()
mymsgid = snmp_reqID_extr()
print(tostring(mymsgid))</code></pre><p>Execution: <code>tshark -X lua_script:snmpreqid.lua -r "snmptrace.pcap"</code></p><p>TSHARK Output:</p><pre><code>nil
nil
nil
...</code></pre><p>The field "snmp.request_id" is correct. I tried to filter out some SNMP V2c Packages in WIRESHARK and it works fine.</p><pre><code>WIRESHARK Filter Expression: snmp.request_id==1959316333
WIRESHARK Package view:
4 SNMP  get-request 1.3.6.1.2.1.1.3  ID: 1959316333
5 SNMP  get-response 1.3.6.1.2.1.1.3 ID: 1959316333</code></pre><p>A test it with the neighbor field "snmp.error_status" was successful</p><pre><code>snmp_reqID_extr = Field.new(&quot;snmp.error_status&quot;)</code></pre><p>TSHARK Output:</p><pre><code>0
0
0
...</code></pre><p>Used WIRESHARK 1.4.2, 1.4.4, 1.5 - problem persists. Read out msgID working at SNMP V3 but not feasible with SNMP V2c because its not implemented in the message header.</p><p>I would be very glad if you could help me on with this problem.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '11, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/ef5f9f91467fe790cfda1a14c69a3b0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="snmpmeier&#39;s gravatar image" /><p><span>snmpmeier</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="snmpmeier has no accepted answers">0%</span></p></div></div><div id="comments-container-2660" class="comments-container"></div><div id="comment-tools-2660" class="comment-tools"></div><div class="clear"></div><div id="comment-2660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

