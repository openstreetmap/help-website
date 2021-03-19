+++
type = "question"
title = "LUA: Accessing protocol values on first scan with tshark -2"
description = '''Hi, I need some clarification regarding the availability of decoded protocol fields when using tshark -2. I have the following test LUA script:  eth_type_f = Field.new(&quot;eth.type&quot;)  luatest = Proto(&quot;luatest&quot;,&quot;luatest Postdissector&quot;)   function luatest.dissector(buffer,pinfo,tree)  if not pinfo.visite...'''
date = "2015-07-27T03:46:00Z"
lastmod = "2015-07-27T05:24:00Z"
weight = 44520
keywords = [ "lua" ]
aliases = [ "/questions/44520" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LUA: Accessing protocol values on first scan with tshark -2](/questions/44520/lua-accessing-protocol-values-on-first-scan-with-tshark-2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44520-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I need some clarification regarding the availability of decoded protocol fields when using tshark -2. I have the following test LUA script:</p><pre><code>  eth_type_f = Field.new(&quot;eth.type&quot;)
  luatest = Proto(&quot;luatest&quot;,&quot;luatest Postdissector&quot;)

  function luatest.dissector(buffer,pinfo,tree)
    if not pinfo.visited then
      info(&quot;not pinfo.visited&quot;)  
      info(&quot;Frame is: &quot; .. pinfo.number)

      local eth_type = eth_type_f()
      x_eth_type = eth_type.value
      info(&quot;x_eth_type: &quot; .. x_eth_type)
    end

    if pinfo.visited then
      info(&quot;pinfo.visited&quot;)  
      info(&quot;Frame is: &quot; .. pinfo.number)

      local eth_type = eth_type_f()
      x_eth_type = eth_type.value
      info(&quot;x_eth_type: &quot; .. x_eth_type)
    end
  end

  -- register our protocol as a postdissector
  register_postdissector(luatest)</code></pre><p>I run the script with the following command:</p><pre><code>tshark -2 -q -X lua_script:&quot;c:\Program Files\Wireshark\plugins\luatest3.lua&quot;  -T fields -E separator=, -E quote=d -e frame.number -e ip.addr -e _ws.col.Info -r tds_sql_batch_first_1.pcapng</code></pre><p>This produces the following output:</p><pre><code>  not pinfo.visited
  Frame is: 1
  pinfo.visited
  Frame is: 1
  x_eth_type: 2048
  &quot;1&quot;,&quot;10.100.20.223,10.100.20.220&quot;,&quot;1155â┼&#39;1433 [ACK] Seq=3698378077 Ack=2551614322 Win=65535 Len=0&quot;</code></pre><p>It seems that the decoded protocol field eth.type is not available in the first scan (when pinfo.visited is false). Is this correct?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '15, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-44520" class="comments-container"></div><div id="comment-tools-44520" class="comment-tools"></div><div class="clear"></div><div id="comment-44520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44521"></span>

<div id="answer-container-44521" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44521-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Correct - both tshark and Wireshark invoke dissection at various times, and in order to improve on performance they don't dissect certain fields if they don't think they need to. So in tshark's case, with the two-pass analysis it doesn't think you need that field information until the second pass. I bet if you set a filter, like '<code>-R "eth.type"</code>', then you'd see it in both passes.</p><p>But anyway there is a work-around for this that should make it work: add the Lua boolean "<code>true</code>" as a second argument to "<code>register_postdissector()</code>", like this:</p><pre><code>-- register our protocol as a postdissector
register_postdissector(luatest, true)</code></pre><p>That should force tshark/wireshark to generate all fields all the time. It impacts performance, which is why it's not enabled by default.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '15, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44521" class="comments-container"><span id="44523"></span><div id="comment-44523" class="comment"><div id="post-44523-score" class="comment-score"></div><div class="comment-text"><p>Hi Hadriel, Adding the Boolean doesn't work - I get the same result as I get without it. The filter works great - thanks for that.</p><p>Best regards...Paul</p></div><div id="comment-44523-info" class="comment-info"><span class="comment-age">(27 Jul '15, 05:43)</span> PaulOfford</div></div><span id="44525"></span><div id="comment-44525" class="comment"><div id="post-44525-score" class="comment-score"></div><div class="comment-text"><p>Hmmm... yet another bug. If you submit another bug for it I'll fix that too.</p></div><div id="comment-44525-info" class="comment-info"><span class="comment-age">(27 Jul '15, 06:15)</span> Hadriel</div></div></div><div id="comment-tools-44521" class="comment-tools"></div><div class="clear"></div><div id="comment-44521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

