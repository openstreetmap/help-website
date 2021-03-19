+++
type = "question"
title = "Extract Value of XML Element"
description = '''Goal: Extract the value of an XML element in SOAP requests. Ideally, I would use this in a custom display column (which I can also export to CSV). Nature of Traffic: The captures contain numerous SOAP requests POSTed over HTTPS. The requests are large, spanning multiple packets. Given the private ke...'''
date = "2015-09-21T08:54:00Z"
lastmod = "2015-09-21T08:54:00Z"
weight = 46021
keywords = [ "xml", "lua", "dissector", "dtd" ]
aliases = [ "/questions/46021" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extract Value of XML Element](/questions/46021/extract-value-of-xml-element)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46021-score" class="post-score" title="current number of votes">0</div><span id="post-46021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Goal: Extract the value of an XML element in SOAP requests. Ideally, I would use this in a custom display column (which I can also export to CSV).</p><p>Nature of Traffic: The captures contain numerous SOAP requests POSTed over HTTPS. The requests are large, spanning multiple packets. Given the private key, Wireshark is already able to decrypt the sessions, assemble the POST request, and dissect the XML. However, there is a many-to-one relationship between dissected fields (xml.tag and xml.cdata) and packets, and I do not know how to navigate this.</p><p>Option #1: I initially investigated writing a Lua Dissector/Tap/Listener (something I have had success with in the past). However, the documentation for Field is missing from the LuaAPI documentation, and I am unable to guess at how to access more than the first element of the XML. I am also unable to guess at how I might register a dissector to be called by the XML dissector. (At this point, I am UTSL, but there are so many abstraction layers in the code, it is going to take me a while.)</p><p>Option #2: I found the Wireshark document on XML, describing the creation of DTDs for Wireshark. It's all very interesting, but it doesn't mention how it is activated. I have tried creating a DTD, and the elements I have added appear as valid identifiers for filter expressions, but no values ever seem to get populated. How does Wireshark know to use my DTD when encountering the XML in the SOAP requests?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-dtd" rel="tag" title="see questions tagged &#39;dtd&#39;">dtd</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '15, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/f8a7cd0d2f97ba95fc9abc1acebad1d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Pearce&#39;s gravatar image" /><p><span>Michael Pearce</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Pearce has no accepted answers">0%</span></p></div></div><div id="comments-container-46021" class="comments-container"></div><div id="comment-tools-46021" class="comment-tools"></div><div class="clear"></div><div id="comment-46021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

