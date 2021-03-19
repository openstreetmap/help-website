+++
type = "question"
title = "using libxml2 in my own dissector"
description = '''Hello,  I am trying to write my own wireshark plugin. I need to use xml library. I modified Makefile.nmake, added all includes and lib files: CFLAGS=$(WARNINGS_ARE_ERRORS) $(STANDARD_CFLAGS) &#92; /I../.. $(GLIB_CFLAGS) &#92; /I$(PCAP_DIR)&#92;include &#92; /Izlib&#92;include &#92; /Ilibxml2&#92;include &#92; /Ilibiconv&#92;include  ....'''
date = "2014-09-08T02:27:00Z"
lastmod = "2014-09-08T18:16:00Z"
weight = 36063
keywords = [ "libxml2", "dissector" ]
aliases = [ "/questions/36063" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [using libxml2 in my own dissector](/questions/36063/using-libxml2-in-my-own-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36063-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to write my own wireshark plugin. I need to use xml library. I modified Makefile.nmake, added all includes and lib files:</p><pre><code>CFLAGS=$(WARNINGS_ARE_ERRORS) $(STANDARD_CFLAGS) \
/I../.. $(GLIB_CFLAGS) \
/I$(PCAP_DIR)\include \
/Izlib\include \
/Ilibxml2\include \
/Ilibiconv\include

.c.obj::
$(CC) $(CFLAGS) -Fd.\ -c $&lt;

LDFLAGS = $(PLUGIN_LDFLAGS)

!IFDEF ENABLE_LIBWIRESHARK
LINK_PLUGIN_WITH=..\..\epan\libwireshark.lib
CFLAGS=$(CFLAGS)

LINK_PLUGIN_WITH=$(LINK_PLUGIN_WITH) zlib\lib\zdll.lib
LINK_PLUGIN_WITH=$(LINK_PLUGIN_WITH) libxml2\lib\libxml2.lib
LINK_PLUGIN_WITH=$(LINK_PLUGIN_WITH) libxml2\lib\libxml2_a.lib
LINK_PLUGIN_WITH=$(LINK_PLUGIN_WITH) libxml2\lib\libxml2_a_dll.lib
LINK_PLUGIN_WITH=$(LINK_PLUGIN_WITH) libiconv\lib\libiconv.lib
LINK_PLUGIN_WITH=$(LINK_PLUGIN_WITH) libiconv\lib\libcharset.lib</code></pre><p>The dissector is a developed as a plugin and runs fine till I added the libxml2 library. After adding libxml2 lib, my dissector is also compiling well, but when I add method which uses libxml2 library and run wireshark I am getting an error:</p><p>" Couldn't load module C:\EWireshark\EWireshark_clean\wireshark-gtk2\plugins\1.99.0\lsd.dll: .. "</p><p>What's more I don't even use this method anywhere in my plugin. It is only written and looks like that:</p><pre><code>void parseMetafile(xmlChar* metafile)
{
        xmlDocPtr doc = xmlParseDoc(metafile); 
}</code></pre><p>After commenting this method out my wireshark plugin works well.</p><p>It seems that it is a problem with some libxml2 dependencies, but I have no idea what more should I add to Makefile.nmake to fix this problem.</p><p>Is there anything to debug this, or does somebody know what I am doing wrong?</p></div><div id="question-tags" class="tags-container tags">libxml2 dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '14, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/4cb7b7ac61efaded7749985daff28985?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Magda%20Nowak-Trzos&#39;s gravatar image" /><p>Magda Nowak-...<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Magda Nowak-Trzos has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Sep '14, 07:46</p></div></div><div id="comments-container-36063" class="comments-container"></div><div id="comment-tools-36063" class="comment-tools"></div><div class="clear"></div><div id="comment-36063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36085"></span>

<div id="answer-container-36085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36085-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>On Windows, explicit DLL dependencies must be satisfied at load time from the DLL search path, which isn't the same as the command path. The error you've reported is symptomatic of an unmet dependency.</p><p>To fix it you will have to copy (or ensure nmake copies) the dependant DLLs somewhere on the DLL search path, the location of your plugin DLL in the 'run' directly is suitable.</p><p>To work out the DLLs required (you many need more than one) you can either copy each one in turn as indicated by the error, or use a tool such as 'depends' to list all the dependencies. The libxml docs might also have more on any dependencies.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '14, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36085" class="comments-container"></div><div id="comment-tools-36085" class="comment-tools"></div><div class="clear"></div><div id="comment-36085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36089"></span>

<div id="answer-container-36089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36089-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will need to add these dlls into the directory in which you are running the executable for libxml2 to be loaded correctly:</p><p>iconv.dll</p><p>libxml2.dll</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '14, 18:16</strong></p><img src="https://secure.gravatar.com/avatar/8e15a601ac7f7d65a3c7926934962bd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frankie&#39;s gravatar image" /><p>Frankie<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frankie has no accepted answers">0%</span></p></div></div><div id="comments-container-36089" class="comments-container"><span id="36097"></span><div id="comment-36097" class="comment"><div id="post-36097-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot ! iconv.dll was missing</p></div><div id="comment-36097-info" class="comment-info"><span class="comment-age">(09 Sep '14, 01:08)</span> Magda Nowak-...</div></div></div><div id="comment-tools-36089" class="comment-tools"></div><div class="clear"></div><div id="comment-36089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

