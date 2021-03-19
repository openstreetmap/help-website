+++
type = "question"
title = "Tap Plugin to 3rd Part Tool with GUI"
description = '''HI, I have a number of custom lua dissectors all of which contain geo positional data. The location in the packets of the geo positional data is not the same in any of the dissectors. What I am trying to do is take the geo positional data out of the packets and get them to a 3rd party applications t...'''
date = "2016-05-16T08:31:00Z"
lastmod = "2016-07-19T09:32:00Z"
weight = 52623
keywords = [ "tap", "plugin" ]
aliases = [ "/questions/52623" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Tap Plugin to 3rd Part Tool with GUI](/questions/52623/tap-plugin-to-3rd-part-tool-with-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52623-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI,</p><p>I have a number of custom lua dissectors all of which contain geo positional data. The location in the packets of the geo positional data is not the same in any of the dissectors. What I am trying to do is take the geo positional data out of the packets and get them to a 3rd party applications that would display the positions all in near real time.</p><p>After reading the development documentation I have a possible design that has a few holes that I would like some feedback on.</p><p>My though was to create a tap plugin that would grab the positional data then send the data to the 3rd party tool. From the README.tapping this appears to be possible.</p><p>Questions:</p><ol><li>What is the best way to get my data out of wireshark from the tap to the 3rd party tool? I was thinking about a QUdpSocket but this will take up time from Wireshark’s normal functions. Maybe I could append data to a file for another application to read? Any recommendations?</li><li>Can a Tap Plugin have a GUI/Preferences that would allow tap customizations of the fields or protocols that the plugin tap registers to? If this is possible can you point me to an example/documentation/functions that I would use to accomplish this?</li></ol><p>Thanks for the help and for making WireShark great.</p></div><div id="question-tags" class="tags-container tags">tap plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '16, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/334b3772ba24e093b1c83a07da9e12c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20B&#39;s gravatar image" /><p>Rob B<br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob B has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '16, 08:45</p></div></div><div id="comments-container-52623" class="comments-container"></div><div id="comment-tools-52623" class="comment-tools"></div><div class="clear"></div><div id="comment-52623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54163"></span>

<div id="answer-container-54163" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54163-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can't you just export the data you need using <code>tshark</code> and <code>-T fields -e field1 -e field2 ...</code>? You can then write the output to a file or pipe it directly to the 3rd party tool if the tool is able to parse it. For example, for normal GeoIP data, you might output something like this:</p><pre><code>tshark.exe -r file.pcap -T fields -e frame.number -e ip.src -e ip.geoip.src_city -e ip.geoip.src_country -e ip.dst -e ip.geoip.dst_city -e ip.geoip.dst_country</code></pre><p>Just replace the fields with the fields you're interested in from your own Lua dissectors.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '16, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54163" class="comments-container"><span id="54245"></span><div id="comment-54245" class="comment"><div id="post-54245-score" class="comment-score"></div><div class="comment-text"><p>I ended using this approach.</p></div><div id="comment-54245-info" class="comment-info"><span class="comment-age">(22 Jul '16, 15:34)</span> Rob B</div></div></div><div id="comment-tools-54163" class="comment-tools"></div><div class="clear"></div><div id="comment-54163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

