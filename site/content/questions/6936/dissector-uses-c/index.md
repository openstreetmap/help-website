+++
type = "question"
title = "Dissector uses C++"
description = '''Hi, I&#x27;m writing a dissector that I&#x27;ve put in the plugins directory. Some of the code being called by my dissector is C++ code. The C++ code has been compiled into a library. Currently, I am calling &quot;make&quot; from my wireshark installation directory, which compiles foo.o with gcc and then attempts to li...'''
date = "2011-10-17T16:49:00Z"
lastmod = "2011-10-17T16:49:00Z"
weight = 6936
keywords = [ "compile", "link", "c++", "dissectors" ]
aliases = [ "/questions/6936" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector uses C++](/questions/6936/dissector-uses-c)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6936-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm writing a dissector that I've put in the plugins directory. Some of the code being called by my dissector is C++ code. The C++ code has been compiled into a library. Currently, I am calling "make" from my wireshark installation directory, which compiles foo.o with gcc and then attempts to link foo.o with my C++ library with gcc as well (to form foo.so). However, I believe I want to use g++ to link, right? Right now after I call "make", I am separately issuing a g++ link command. Is there any clever way to integrate the g++ link command into the "make" so that I don't have to link with a separate call?</p><p>Also, I'm not too familiar with shared objects. It looks like any library I link in has to be compiled with the -fPIC flag - is that right?</p></div><div id="question-tags" class="tags-container tags">compile link c++ dissectors</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '11, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/851676df3c7a09999c0522099f40d6e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JVo&#39;s gravatar image" /><p>JVo<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JVo has no accepted answers">0%</span></p></div></div><div id="comments-container-6936" class="comments-container"><span id="6945"></span><div id="comment-6945" class="comment"><div id="post-6945-score" class="comment-score"></div><div class="comment-text"><p>I really dont know the answer but can share some knowledge...</p><h1 id="ifdef-__cplusplus">ifdef __cplusplus</h1><p>extern "C" {</p><h1 id="endif-__cplusplus">endif / <em>__cplusplus</em> /</h1><p>This code is present in some of the header files which will allow the cplusplus code to sync up with the C.</p></div><div id="comment-6945-info" class="comment-info"><span class="comment-age">(18 Oct '11, 01:32)</span> Terrestrial ...</div></div><span id="6960"></span><div id="comment-6960" class="comment"><div id="post-6960-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Yes, I am using the ifdef _cplusplus extern "C" code. But if anybody can help answer either of the other questions, that would be great.</p></div><div id="comment-6960-info" class="comment-info"><span class="comment-age">(18 Oct '11, 10:01)</span> JVo</div></div></div><div id="comment-tools-6936" class="comment-tools"></div><div class="clear"></div><div id="comment-6936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

