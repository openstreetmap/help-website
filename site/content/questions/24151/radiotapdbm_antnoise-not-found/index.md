+++
type = "question"
title = "radiotap.dbm_antnoise not found"
description = '''First of all, I&#x27;m monitoring my wifi network in monitor/promiscuous mode. On my Mac I have wireshark / tshark v1.10.1 On a debian machine I have tshark 1.10.2 I noticed that on my Mac I can capture &quot;radiotap.dbm_antnoise&quot; which is the antenna noise, but on my debian machine it does not show up (whet...'''
date = "2013-08-28T11:18:00Z"
lastmod = "2013-08-28T11:30:00Z"
weight = 24151
keywords = [ "promiscuous", "dbmantnoise", "tshark", "monitor" ]
aliases = [ "/questions/24151" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [radiotap.dbm\_antnoise not found](/questions/24151/radiotapdbm_antnoise-not-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24151-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First of all, I'm monitoring my wifi network in monitor/promiscuous mode.</p><p>On my Mac I have wireshark / tshark v1.10.1</p><p>On a debian machine I have tshark 1.10.2</p><p>I noticed that on my Mac I can capture "radiotap.dbm_antnoise" which is the antenna noise, but on my debian machine it does not show up (whether I capture as an XML file or specify "radiotap.dbm_antnoise")</p><p>I was originally running an older version of tshark that I'd installed from aptitude, thought that was the problem, so I uninstalled that and just finished compiling 1.10.2 from source (which didn't help).</p><p>This is the command I'm running:</p><p>sudo tshark -I -i myinterface -Y "wlan.fc.type_subtype == 0x04" -T fields -E separator=, -E quote=d -e "wlan.sa" -e "frame.time_epoch" -e "radiotap.dbm_antsignal" -e "radiotap.dbm_antnoise"</p><p>Here are the results:</p><p>On my Mac:</p><p>Capturing on 'Wi-Fi'</p><p>"e1:c2:df:f9:33:07","1377713656.454545000","-71","-88"</p><p>(looks OK)</p><p>But on the debian machine:</p><p>Capturing on 'wlan0'</p><p>"a4:d1:d2:e5:86:d0","1377713603.090254000","-87",</p><p>(Notice how the last field is empty)</p><p>Does anyone know why this could be happening?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">promiscuous dbmantnoise tshark monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '13, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/136f4e7a28be42183b8234777b9fdfdf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jjardine&#39;s gravatar image" /><p>jjardine<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jjardine has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Aug '13, 11:22</p></div></div><div id="comments-container-24151" class="comments-container"></div><div id="comment-tools-24151" class="comment-tools"></div><div class="clear"></div><div id="comment-24151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24152"></span>

<div id="answer-container-24152" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24152-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This field will be present only if your Wifi adapter on your Linux box does provide this information. My guess is that your adapter does not support this metric. This can be checked with the radiotap.present.dbm_antnoise value.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '13, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-24152" class="comments-container"><span id="24153"></span><div id="comment-24153" class="comment"><div id="post-24153-score" class="comment-score"></div><div class="comment-text"><p>Thanks! That makes sense. I guess I will try to find a better device for my Linux box.</p><p>For the record, this is what my adapter shows up as under lsusb:</p><p>Bus 001 Device 003: ID 148f:5370 Ralink Technology, Corp. RT5370 Wireless Adapter</p><p>and also no luck with this guy:</p><p>Bus 001 Device 014: ID 0bda:8178 Realtek Semiconductor Corp. RTL8192CU 802.11n WLAN Adapter</p></div><div id="comment-24153-info" class="comment-info"><span class="comment-age">(28 Aug '13, 11:35)</span> jjardine</div></div></div><div id="comment-tools-24152" class="comment-tools"></div><div class="clear"></div><div id="comment-24152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

