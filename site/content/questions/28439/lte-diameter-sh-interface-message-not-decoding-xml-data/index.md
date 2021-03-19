+++
type = "question"
title = "LTE Diameter Sh interface message not Decoding XML Data"
description = '''Im not able to view the user Data which comes as XML in Diameter messages between PCRF and SPR on diameter Sh interface for eg PUR,UDA messages of Diameter,only third window shows that info which is difficult to view.'''
date = "2013-12-27T06:41:00Z"
lastmod = "2013-12-28T06:57:00Z"
weight = 28439
keywords = [ "xml", "diameter" ]
aliases = [ "/questions/28439" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LTE Diameter Sh interface message not Decoding XML Data](/questions/28439/lte-diameter-sh-interface-message-not-decoding-xml-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28439-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im not able to view the user Data which comes as XML in Diameter messages between PCRF and SPR on diameter Sh interface for eg PUR,UDA messages of Diameter,only third window shows that info which is difficult to view.</p></div><div id="question-tags" class="tags-container tags">xml diameter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '13, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/4ca65c5e2c6c0dab0e0f3eb1a040023f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mayoor&#39;s gravatar image" /><p>mayoor<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mayoor has no accepted answers">0%</span></p></div></div><div id="comments-container-28439" class="comments-container"><span id="28442"></span><div id="comment-28442" class="comment"><div id="post-28442-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark are you using? It might work in 1.10.x</p></div><div id="comment-28442-info" class="comment-info"><span class="comment-age">(27 Dec '13, 08:19)</span> Anders ♦</div></div><span id="28455"></span><div id="comment-28455" class="comment"><div id="post-28455-score" class="comment-score"></div><div class="comment-text"><p>This might sound picky of me, I know, but Sh is an IMS interface, not an LTE interface. While I'll grudgingly accept the radio network technology that is the EUTRAN being called by the name of the project that created it (LTE), I'll grin and bare EPC being referred to as the name of that radio access project that didn't create it, and I'll even contend with the whole EPS being collectively referred to as the name of that one radio access project, and as "4G" LTE to boot, but IMS interfaces? No - the line must be drawn.</p><p>IMS is Release 5 and is years older than the LTE project, as is the Sh interface. It wasn't all that popular, but dammit it existed. The EPC was intended to be as radio-agnostic as it could be, IMS is for the most part agnostic to the IP access method toward it (such as the EPC), yet somehow the LTE terminology virus is consuming all other technical systems that it expands into. If we give up this ground the Internet itself is in jeopardy.</p><p>/rant</p></div><div id="comment-28455-info" class="comment-info"><span class="comment-age">(27 Dec '13, 19:01)</span> Quadratic</div></div><span id="28456"></span><div id="comment-28456" class="comment"><div id="post-28456-score" class="comment-score"></div><div class="comment-text"><p>Andres im using 1.10.5 and pumping traffic from seagull simulator,in user data AVP im getting User-Data as 3c5265706f73697..</p></div><div id="comment-28456-info" class="comment-info"><span class="comment-age">(28 Dec '13, 05:29)</span> mayoor</div></div><span id="28457"></span><div id="comment-28457" class="comment"><div id="post-28457-score" class="comment-score"></div><div class="comment-text"><p>@Quadratic as per 3GPP 23.203 PCC architecture has SPR and we are testing Sp/Sh interface ,PCRF connected with AF which is referred as IMS node</p></div><div id="comment-28457-info" class="comment-info"><span class="comment-age">(28 Dec '13, 05:31)</span> mayoor</div></div><span id="28459"></span><div id="comment-28459" class="comment"><div id="post-28459-score" class="comment-score"></div><div class="comment-text"><p>Yes Mayoor, that's what I'm saying, it's an IMS interface. It can be linked to the PcC architecture used by the EPC, which is also not tied to LTE.</p><p>LTE was a radio project, the resulting radio network (EUTRAN) kept its name, then the EPC (from the SAE project) started getting tagged as the "LTE Core", so EPS itself was taken over by that term, and now (not just you, a lot of people in the industry) are tying IMS nodes and interfaces with the term "LTE". Thus we have the name of a radio project now expanding itself into an access-agnostic SIP/RTP service network.</p><p>I know its not an answer to the question, just a comment but we must stop calling everything LTE.</p></div><div id="comment-28459-info" class="comment-info"><span class="comment-age">(28 Dec '13, 07:19)</span> Quadratic</div></div><span id="31513"></span><div id="comment-31513" class="comment not_top_scorer"><div id="post-31513-score" class="comment-score"></div><div class="comment-text"><p>thumbs up quadratic. yes Sh is an IMS interface, (HSS-AS), EPC is more apt term than LTE. :)</p></div><div id="comment-31513-info" class="comment-info"><span class="comment-age">(04 Apr '14, 08:36)</span> Sanny_D</div></div></div><div id="comment-tools-28439" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-28439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28458"></span>

<div id="answer-container-28458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28458-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The diameter 3GPP sub dissector expects the content to start with "&lt;?xml"</p><p>3GPP 3GPP TS 29.329</p><p>6.3.3 User-Data AVP The User-Data AVP is of type OctetString. This AVP contains the user data requested in the PUR and SNR operations and the data to be modified in the UPR operation . The exact content and format of this AVP is described in 3GPP TS 29.328 [1].</p><p>7.6 Data This information element contains an XML document conformant to the XML schema defined in Annex D. Annex C specifies the UML logical model of the data downloaded via the Sh interface.</p><p>So I suspect your data is malformed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '13, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-28458" class="comments-container"><span id="28468"></span><div id="comment-28468" class="comment"><div id="post-28468-score" class="comment-score"></div><div class="comment-text"><p>when i copy/paste the data from User Data to notepad then it is decoded successfully,so i believe it is not corrupted for eg &lt;repositorydata&gt;&lt;serviceindication&gt;CamiantUserData&lt;/serviceindication&gt;&lt;sequencenumber&gt;1&lt;/sequencenumber&gt;&lt;servicedata&gt;&lt;![CDATA[&lt;?xml version="1.0"encoding="UTF-8"?&gt;&lt;subscriber&gt;&lt;fieldname="msisdn"&gt;918802856800&lt;/field&gt;&lt;fieldname="billingday"&gt;30&lt;/field&gt;&lt;fieldname="tier"&gt;Diamond&lt;/field&gt;&lt;fieldname="entitlement"&gt;1&lt;/field&gt;&lt;fieldname="entitlement"&gt;2&lt;/field&gt;&lt;fieldname="entitlement"&gt;3&lt;/field&gt;&lt;fieldname="entitlement"&gt;Video&lt;/field&gt;&lt;fieldname="custom1"&gt;301&lt;/field&gt;&lt;fieldname="custom2"&gt;401&lt;/field&gt;&lt;fieldname="custom3"&gt;501&lt;/field&gt;&lt;fieldname="custom4"&gt;office&lt;/field&gt;&lt;/subscriber&gt;]]&gt;&lt;/servicedata&gt;&lt;/repositorydata&gt;</p></div><div id="comment-28468-info" class="comment-info"><span class="comment-age">(28 Dec '13, 21:44)</span> mayoor</div></div><span id="28470"></span><div id="comment-28470" class="comment"><div id="post-28470-score" class="comment-score"></div><div class="comment-text"><p>I don't think your data is a "proper" xml document. I think it should look something like</p><p>&lt;sh-data&gt;&lt;publicidentifiers&gt;&lt;imspublicidentity&gt; : &lt;/sh-data&gt;</p><p>e.g the xml document should srt with &lt;?xml version</p></div><div id="comment-28470-info" class="comment-info"><span class="comment-age">(29 Dec '13, 01:22)</span> Anders ♦</div></div><span id="28471"></span><div id="comment-28471" class="comment"><div id="post-28471-score" class="comment-score"></div><div class="comment-text"><p>That did not come out right: &lt;?xml version="1.0" encoding="UTF-8"?&gt; &lt;sh-data&gt; : &lt;/sh-data&gt;</p></div><div id="comment-28471-info" class="comment-info"><span class="comment-age">(29 Dec '13, 01:23)</span> Anders ♦</div></div></div><div id="comment-tools-28458" class="comment-tools"></div><div class="clear"></div><div id="comment-28458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

