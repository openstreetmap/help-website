+++
type = "question"
title = "Recursive XML DTD"
description = '''I have some proprietary HTTP/XML that I was wanting Wireshark to be able to parse and use as a display filter, so I started writing a DTD that Wireshark could deal with. It seems to work until I get to the second instance of an element in the filter, at which point it claims that the filter is inval...'''
date = "2014-02-04T10:00:00Z"
lastmod = "2014-02-04T10:00:00Z"
weight = 29435
keywords = [ "xml", "dtd", "display-filter" ]
aliases = [ "/questions/29435" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Recursive XML DTD](/questions/29435/recursive-xml-dtd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29435-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some proprietary HTTP/XML that I was wanting Wireshark to be able to parse and use as a display filter, so I started writing a DTD that Wireshark could deal with. It seems to work until I get to the second instance of an element in the filter, at which point it claims that the filter is invalid.</p><p>This is the DTD I've generated:</p><pre><code>&lt;?wireshark:protocol proto_name=&quot;myxml&quot; hierarchy=&quot;yes&quot; ?&gt;
&lt;!ELEMENT methodCall (methodName,params) &gt;
&lt;!ELEMENT methodName (#PCDATA) &gt;
&lt;!ELEMENT params (param+) &gt;
&lt;!ELEMENT param (value) &gt;
&lt;!ELEMENT value (array|string|struct) &gt;
&lt;!ELEMENT struct (member) &gt;
&lt;!ELEMENT member (name,value) &gt;
&lt;!ELEMENT name (#PCDATA) &gt;
&lt;!ELEMENT array (data+) &gt;
&lt;!ELEMENT data (value) &gt;
&lt;!ELEMENT string (#PCDATA) &gt;</code></pre><p>(No comments about the ridiculousness of this structure; I'm documenting someone else's crap, not defining it.)</p><p>The filter I'm trying to write is:</p><pre><code>myxml.params.param.value.struct.member.value</code></pre><p>It works if I leave the last <code>value</code> off, and it works if I use <code>name</code> instead of the last <code>value</code>.</p><p>On the <a href="http://wiki.wireshark.org/XML">XML entry in the Wireshark Wiki</a>, it says:</p><blockquote><p>Recursion in elements is stopped abruptly the second time the same element is found a "root name" will be used instead.</p></blockquote><p>It is unclear if that is in the context of the <code>hierarchy</code> attribute that it immediately follows, or if it's a new thought, despite the fact that elements aren't introduced in the document until later. Also, it's not a valid English sentence, which makes it that much harder to understand. (It may need nothing more than a period, but I'm not sure.)</p><p>I have the feeling that it's trying to say that using recursion in an XML/DTD filter is unsupported, and has nothing to do with setting the <code>hierarchy</code> option or not. Can anyone confirm or deny Wireshark's ability to use recursive XML/DTD filters?</p></div><div id="question-tags" class="tags-container tags">xml dtd display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '14, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/b1fcb959367f49735c560606f5cfb5f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wfaulk&#39;s gravatar image" /><p>wfaulk<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wfaulk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '14, 10:04</p></div></div><div id="comments-container-29435" class="comments-container"></div><div id="comment-tools-29435" class="comment-tools"></div><div class="clear"></div><div id="comment-29435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

