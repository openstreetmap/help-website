+++
type = "question"
title = "Get value of node &quot;hf_foo_flags&quot;, &quot;hf_camel_general&quot;, ...etc..."
description = '''Hi all, I follow the guide of Developers (http://www.wireshark.org/download/docs/developer-guide-a4.pdf) and in the chapter 9, I&#x27;m trying to understand the code structure of wireshark. In the code Example 9.8. &quot;Wrapping up the packet dissection&quot;, I see &quot;proto-register-foo(void)&quot; in which we have:   ...'''
date = "2013-09-06T03:26:00Z"
lastmod = "2013-09-06T08:22:00Z"
weight = 24416
keywords = [ "node", "index", "packet-foo" ]
aliases = [ "/questions/24416" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get value of node "hf\_foo\_flags", "hf\_camel\_general", ...etc...](/questions/24416/get-value-of-node-hf_foo_flags-hf_camel_general-etc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24416-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I follow the guide of Developers (<a href="http://www.wireshark.org/download/docs/developer-guide-a4.pdf)">http://www.wireshark.org/download/docs/developer-guide-a4.pdf)</a> and in the chapter 9, I'm trying to understand the code structure of wireshark. In the code Example 9.8. "Wrapping up the packet dissection", I see "proto-register-foo(void)" in which we have:</p><hr /><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_5.PNG" alt="Code" /></p><hr /><p>where "hf_foo_flags" is the index for this node. I wonder how we can get the value of this node, in other words, I want to export this value into text file and apply to all of those nodes. But it seems to be just an INDEX for this node, not value. So, experts, Could you please explain to me how to get the value of this node? Thanks !</p></div><div id="question-tags" class="tags-container tags">node index packet-foo</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '13, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p>hoangsonk49<br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 06 Sep '13, 08:11</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-24416" class="comments-container"><span id="24419"></span><div id="comment-24419" class="comment"><div id="post-24419-score" class="comment-score"></div><div class="comment-text"><p>I think you need to explain in more detail what you are trying to do as I suspect you are going about it in the wrong way. tshark -z might do what you are looking for.</p></div><div id="comment-24419-info" class="comment-info"><span class="comment-age">(06 Sep '13, 04:47)</span> Anders ♦</div></div><span id="24423"></span><div id="comment-24423" class="comment"><div id="post-24423-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders, Here is some values which are dissector-ed by GUI</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_6.PNG" alt="alt text" /></p><p>Each ones has its own value, for example servicekey = 20, that 's what we can see on GUI.My objective is to extract those values into text file AUTOMATICALLY by using source code, not tshark -z, or copy-paste from GUI... Of course Tshark -z can do it but I want to go deeper, into lower level which is really running inside the command of tshark, in other words, I have to control the flow of Wireshark and where it assigns those values in the code. I check in the code and see that all values have its node. For example: "FOO PDF Flags" has "hf-foo-flags", "servicekey" has "hf-camel-serviceKey". But that is not a variable which carry its value, it is just an index of a node. So, I have a node index, I wonder how to get the value of this node. In genetal my question is:</p><ol><li><p>Which variable in the code carry the value of things like "servicekey, locationnumber, FOO PDF Flags ..."?</p></li><li><p>As I see, Each things like "servicekey, locationnumber, FOO PDF Flags ..." has its own node index such as "hf-camel-serviceKey, hf-foo-flags" but I don't know how to fprintf the value of this node. I guess the value of this node is value of those things which are displayed on GUI, so I need to print out to be sure.</p></li></ol><p>Please help if you have any idea about it, thanks a lot. Note: "hf-foo-flags" means "hf (underline) foo(underline) flags" because this box ignores that format :)</p></div><div id="comment-24423-info" class="comment-info"><span class="comment-age">(06 Sep '13, 06:04)</span> hoangsonk49</div></div><span id="24425"></span><div id="comment-24425" class="comment"><div id="post-24425-score" class="comment-score"></div><div class="comment-text"><p>Well a full protocol tre might not be built on the first sequential pass trough the capture file by wireshark so even accessing the tree might not give you what you want. Parsing the PDML output might be an idea.</p></div><div id="comment-24425-info" class="comment-info"><span class="comment-age">(06 Sep '13, 06:47)</span> Anders ♦</div></div><span id="24462"></span><div id="comment-24462" class="comment"><div id="post-24462-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders, but when we open GUI and "start" to run, "Parsing The PDML" doesn't run in parallel, right? "Parsing The PDML" starts to run only when we use command to call it in order to export PDML file. So, it means, to display the value "20" of "servicekey", Wireshark must get this value from somewhere in the code, right? And I'm looking for that "somewhere". Wireshare processes the dissector by the file "packet-xxx.c" where xxx is the name of protocol. Processing is done in this file, but all i know is that it puts the value into a tree and i don't know how it get these values from the tree to display. In other words, which function get and display the value of "serviceKey" on GUI</p></div><div id="comment-24462-info" class="comment-info"><span class="comment-age">(08 Sep '13, 18:48)</span> hoangsonk49</div></div></div><div id="comment-tools-24416" class="comment-tools"></div><div class="clear"></div><div id="comment-24416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24428"></span>

<div id="answer-container-24428" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24428-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe using <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> gives you what you want?</p><pre><code>tshark -r file.pcap -T fields -e camel.serviceKey -e camel.locationNumber</code></pre><p>Feel free to add as many fields as needed.</p><p>In Wireshark, you could add those fields of interest as custom columns via <code>Edit -&gt; Preferences -&gt; Columns -&gt; Add -&gt; Field type: Custom -&gt; Field name: camel.serviceKey -&gt; [Rename title and drag to desired column location] -&gt; OK</code>, and then use <code>File -&gt; Export Packet Dissections -&gt; as "Plain Text" file... -&gt; Packet summary line</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '13, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></img></div></div><div id="comments-container-24428" class="comments-container"><span id="24461"></span><div id="comment-24461" class="comment"><div id="post-24461-score" class="comment-score"></div><div class="comment-text"><p>Hi cmaynard, Yes, of course, TSHARK can do it as well, but as I mentioned above, I 'd like to control it at lower level, by source code, not only by command Tshark in order to do more with these values. So, to do that I have to know which variable carry those values, that 's all what I am looking for. Thanks!</p></div><div id="comment-24461-info" class="comment-info"><span class="comment-age">(08 Sep '13, 18:05)</span> hoangsonk49</div></div></div><div id="comment-tools-24428" class="comment-tools"></div><div class="clear"></div><div id="comment-24428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

