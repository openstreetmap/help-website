+++
type = "question"
title = "lte rrc decoding using lua script"
description = '''Hi All,  I&#x27;m new to lua script development. I&#x27;m trying to get dissector = Dissector.get(lte-rrc.bcch.bch) but getting error &quot;No such dissector&quot; .I want to decode lte RRC message by identifying logical channel that is &quot;on UDP port number 9999 will be receiving : 1 byte (Logical channel detail) + lte ...'''
date = "2016-06-07T07:05:00Z"
lastmod = "2016-06-07T08:38:00Z"
weight = 53281
keywords = [ "lua", "lte-rrc" ]
aliases = [ "/questions/53281" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lte rrc decoding using lua script](/questions/53281/lte-rrc-decoding-using-lua-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53281-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I'm new to lua script development. I'm trying to get dissector = Dissector.get(lte-rrc.bcch.bch) but getting error "No such dissector" .I want to decode lte RRC message by identifying logical channel that is "on UDP port number 9999 will be receiving : 1 byte (Logical channel detail) + lte RRC Hex dump" based on 1st byte need to decode lte RRC hex dump. can you please help me on this . Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">lua lte-rrc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '16, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/06b10c7b143baa866930afe940b84c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Senthil&#39;s gravatar image" /><p>Senthil<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Senthil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jun '16, 07:06</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53281" class="comments-container"></div><div id="comment-tools-53281" class="comment-tools"></div><div class="clear"></div><div id="comment-53281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53284"></span>

<div id="answer-container-53284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53284-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's strange you get a different error than me (maybe a different Wireshark version), but the mistake you've made are just the missing quotes around the dissector name, you have to use</p><pre><code>dissector = Dissector.get(&quot;lte-rrc.bcch.bch&quot;)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '16, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53284" class="comments-container"><span id="53299"></span><div id="comment-53299" class="comment"><div id="post-53299-score" class="comment-score"></div><div class="comment-text"><p>Thanks sindy. Now i am not getting this error. I have a follow up question: Not seeing any impact when I'm using <code>tshark -r lte.pcap -X lua_script:sample.lua -X 'read_format:sample'</code>. My Code is below (modified the code based on available example in internet), please help me on this</p><pre><code>do
  myrrc_proto = Proto(&quot;myrrc&quot;,&quot;myrrc&quot;,&quot;myrrc Protocol&quot;)

  function myrrc_proto.init()
    myrrc = {
      [0] = Dissector.get(&quot;lte-rrc.ul.ccch&quot;),
      [1] = Dissector.get(&quot;lte-rrc.dl.ccch&quot;),
      [2] = Dissector.get(&quot;lte-rrc.pcch&quot;),
      [3] = Dissector.get(&quot;lte-rrc.bcch.bch&quot;),
      [4] = Dissector.get(&quot;lte-rrc.bcch.dl.sch&quot;),
      [5] = Dissector.get(&quot;lte-rrc.ul.dcch&quot;),
      [6] = Dissector.get(&quot;lte-rrc.ul.dcch&quot;),
    }
  end

  function myrrc_proto.dissector(buffer,pinfo,tree)
    local msgtype = buffer(0,1):uint()
    local payload = buffer(1):tvb()
    local dissector=myrrc[msgtype]
    pinfo.cols.protocol =dissector
    myrrc[msgtype].dissector:call(payload,pinfo,tree)
  end

  local wtap_encap_table = DissectorTable.get(&quot;wtap_encap&quot;)
  wtap_encap_table:add(wtap.USER1, myrrc_proto)

end</code></pre></div><div id="comment-53299-info" class="comment-info"><span class="comment-age">(07 Jun '16, 20:01)</span> Senthil</div></div><span id="53302"></span><div id="comment-53302" class="comment"><div id="post-53302-score" class="comment-score"></div><div class="comment-text"><p>House rules: any Answer must answer the original Question, all other posts are Comments. See site FAQ for details on this one and for other house rules.</p><p>Now I don't understand what exactly did you expect to happen when you've used <code>-X 'read_format:sample'</code>. Can you publish an example of your lte.pcap file (of at least several packets)? Normally the preferred way to publish captures is to upload them to Cloudshark, but as your one may be in an unusual format, any plain file sharing service (Dropbox, Google drive, ...) is a better option in this exceptional case. Files have to be published login-free, that's why I mention "several packets" if you are afraid of any privacy issues.</p></div><div id="comment-53302-info" class="comment-info"><span class="comment-age">(07 Jun '16, 22:43)</span> sindy</div></div></div><div id="comment-tools-53284" class="comment-tools"></div><div class="clear"></div><div id="comment-53284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

