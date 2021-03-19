+++
type = "question"
title = "packet export for wlan.sa and wlan.da have two mac addresses separated by a comma"
description = '''I&#x27;ve been doing some wifi performance analysis. Capture performed in monitor mode, exported using tshark as follows: tshark -t r -n -r $1 -E header=y -E separator=&quot;|&quot; -T fields -e frame.time_epoch -e wlan.ta -e wlan.sa -e wlan.ra -e wlan.da -e wlan.bssid -e radiotap.datarate -e radiotap.mcs.index -e...'''
date = "2016-06-26T21:49:00Z"
lastmod = "2016-06-26T21:49:00Z"
weight = 53662
keywords = [ "separated", "mac", "comman", "wlan.sa", "addresses" ]
aliases = [ "/questions/53662" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packet export for wlan.sa and wlan.da have two mac addresses separated by a comma](/questions/53662/packet-export-for-wlansa-and-wlanda-have-two-mac-addresses-separated-by-a-comma)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53662-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been doing some wifi performance analysis. Capture performed in monitor mode, exported using tshark as follows:</p><p><code>tshark -t r -n -r $1 -E header=y -E separator="|" -T fields -e frame.time_epoch -e wlan.ta -e wlan.sa -e wlan.ra -e wlan.da -e wlan.bssid -e radiotap.datarate -e radiotap.mcs.index -e radiotap.vht.datarate.0 -e radiotap.vht.mcs.0 -e radiotap.xchannel -e radiotap.channel.freq -e radiotap.dbm_antsignal -e _ws.col.Protocol -e frame.len -e _ws.col.Info | sed 's/||"/|NA|/g' | sed 's/||/|NA|/g' | sed 's/||/|NA|/g' | sed 's/||/|NA|/g' &gt; $outFile</code></p><p>This is a downstream capture showing traffic from an</p><p>Reference PC on GigE 68:5b:35:cd:ef:ab<br />
Router wirless interface on 5G: f4:f2:6d:ab:cd:ef<br />
Client device (Mac Book Air): 8c:29:37:00:01:02<br />
</p><p>The data packets are showing up with two mac addresses in the SA and DA fields. For the wlan.sa field I see the router,reference PC: <code>"f4:f2:6d:ab:cd:ef,68:5b:35:cd:ef:ab"</code> The wlan.da address shows up as: <code>"8c:29:37:00:01:02,8c:29:37:00:01:02"</code></p><p>Here is a sample of the output from my tshark extraction routine <code>1466826268.835444000|f4:f2:6d:ab:cd:ef|f4:f2:6d:ab:cd:ef,68:5b:35:cd:ef:ab|8c:29:37:00:01:02|8c:29:37:00:01:02,8c:29:37:00:01:02|f4:f2:6d:ab:cd:ef|||526.6|6|149|5745||802.11|3128|QoS Data</code></p><p>Why do the wlan.sa and wlan.da fields have a 2nd MAC or is this a valid output?</p><p>Thanks!</p><p>John</p></div><div id="question-tags" class="tags-container tags">separated mac comman wlan.sa addresses</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '16, 21:49</strong></p><img src="https://secure.gravatar.com/avatar/bb70bb51d803b91016188573b93483cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jpomeroy&#39;s gravatar image" /><p>jpomeroy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jpomeroy has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jun '16, 23:23</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></br></p></div></div><div id="comments-container-53662" class="comments-container"></div><div id="comment-tools-53662" class="comment-tools"></div><div class="clear"></div><div id="comment-53662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

