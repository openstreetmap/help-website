+++
type = "question"
title = "I want to use asn1 module to decode mms packet in my program."
description = '''Hi, everyone.  I make packet monitoring program which monitors particular packets including mms packet. So I want to use asn1 module for mms. I, however, don&#x27;t know where is start point to do that. I successed to compile wireshark by MSVC2008 using nmake. And In my project(this program used mfc), I ...'''
date = "2011-08-26T04:35:00Z"
lastmod = "2011-08-26T04:35:00Z"
weight = 5883
keywords = [ "development" ]
aliases = [ "/questions/5883" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I want to use asn1 module to decode mms packet in my program.](/questions/5883/i-want-to-use-asn1-module-to-decode-mms-packet-in-my-program)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5883-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, everyone.</p><p>I make packet monitoring program which monitors particular packets including mms packet.</p><p>So I want to use asn1 module for mms. I, however, don't know where is start point to do that.</p><p>I successed to compile wireshark by MSVC2008 using nmake.</p><p>And In my project(this program used mfc), I included asn.1, config.h and other code needed for this, and then follow error was appeared.</p><p>"fatal error C1189: #error : Your MSVC_VARIANT setting in config.nmake doesn't match the MS compiler version! F:YangProgramingC &amp; C++librarywireshark-1.6.1wireshark-1.6.1config.h 267 PacketAnalyzer""</p><p>I guess the problem is the compiler that I used is VS MFC compiler that is different with MSVC2008 using "namake".</p><p>Summary, I have two question. The first question is "Can't I include and use asn1 module of wireshark for my mfc program?"</p><p>If that is impossible, where do I start to make my own program using asn1 module of wireshark using nmake?</p></div><div id="question-tags" class="tags-container tags">development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '11, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/528f8dd6acb92d7bc6189be06e46c5cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="one%20step&#39;s gravatar image" /><p>one step<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="one step has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Aug '11, 14:32</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5883" class="comments-container"><span id="5892"></span><div id="comment-5892" class="comment"><div id="post-5892-score" class="comment-score"></div><div class="comment-text"><p>Wireshark has an MMS dissector generated from asn1 files with asn2wrs, isn't that good enough?</p></div><div id="comment-5892-info" class="comment-info"><span class="comment-age">(26 Aug '11, 13:23)</span> Anders ♦</div></div></div><div id="comment-tools-5883" class="comment-tools"></div><div class="clear"></div><div id="comment-5883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

