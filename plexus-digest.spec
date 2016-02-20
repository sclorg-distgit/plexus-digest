%global pkg_name plexus-digest
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global parent plexus
%global subname digest

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.1
Release:        15.10%{?dist}
Epoch:          0
Summary:        Plexus Digest / Hashcode Components
License:        ASL 2.0
URL:            http://plexus.codehaus.org/plexus-components/plexus-digest/
Source0:        %{pkg_name}-%{version}-src.tar.gz
# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-digest-1.1/ plexus-digest/
# tar czf plexus-digest-1.1-src.tar.gz plexus-digest/

Patch0:         %{pkg_name}-migration-to-component-metadata.patch
Patch1:         %{pkg_name}-fix-test-dependencies.patch
Patch2:         0001-Do-not-use-algorithm-name-as-regular-expression.patch

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}ant >= 0:1.6
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-maven-compiler-plugin
BuildRequires:  maven30-maven-install-plugin
BuildRequires:  maven30-maven-jar-plugin
BuildRequires:  maven30-maven-javadoc-plugin
BuildRequires:  maven30-maven-resources-plugin
BuildRequires:  maven30-maven-surefire-plugin
BuildRequires:  maven30-maven-surefire-provider-junit
BuildRequires:  %{?scl_prefix_java_common}qdox >= 1.5
BuildRequires:  maven30-plexus-containers-component-metadata
BuildRequires:  maven30-plexus-cdc


%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
Javadoc for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_file  : %{parent}/%{subname}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/plexus
%dir %{_javadir}/plexus

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 0:1.1-15.10
- maven33 rebuild

* Fri Jan 16 2015 Michal Srb <msrb@redhat.com> - 0:1.1-15.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:1.1-15.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0:1.1-15.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1-15.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1-15.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1-15.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1-15.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1-15.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1-15.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 01.1-15
- Mass rebuild 2013-12-27

* Fri Sep 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1-14
- Do not use algorithm name as regular expression

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1-13
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 0:1.1-12
- Remove unnecessary BR on maven-doxia and maven-doxia-sitetools

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.1-11
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 0:1.1-10
- Build with xmvn

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1-8
- Fix test dependencies

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1-6
- Rebuild for java 1.6.0 downgrade (fesco ticket 663)

* Tue Jul 26 2011 Jaromir Capik <jcapik@redhat.com> - 0:1.1-5
- Migration from plexus-maven-plugin to plexus-containers-component-metadata
- Minor spec file changes according to the latest guidelines

* Sun Jun 12 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.1-4
- Build with maven 3.x

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.1-2
- Drop ant build.
- Adapt to new guidelines.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.1-1
- Update to upstream 1.1.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-10
- Drop not needed depmap.
- Build with maven.

* Fri Aug 21 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-9
- Fix License, formatting and comments.

* Sun May 17 2009 Fernando Nasser <fnasser@redhat.com> 0:1.0-8
- Fix license

* Tue Apr 30 2009 Yong Yang <yyang@redhat.com> 1.0-7
- Rebuild with new maven2 2.0.8 built in non-bootstrap mode

* Tue Apr 30 2009 Yong Yang <yyang@redhat.com> 1.0-6
- force to BR plexus-cdc alpha 10
- rebuild without maven

* Tue Apr 30 2009 Yong Yang <yyang@redhat.com> 1.0-5
- Add BRs maven-doxia*, qdox
- Enable jpp-depmap
- Rebuild with new maven2 2.0.8 built in non-bootstrap mode
- ignore test failure

* Tue Mar 17 2009 Yong Yang <yyang@redhat.com> 1.0-4
- rebuild with new maven2 2.0.8 built in bootstrap mode

* Thu Feb 05 2009 Yong Yang <yyang@redhat.com> 1.0-3
- Fix release tag

* Wed Jan 14 2009 Yong Yang <yyang@redhat.com> 1.0-2jpp.1
- Import from dbhole's maven 2.0.8 packages, initial building

* Mon Jan 07 2008 Deepak Bhole <dbhole@redhat.com> 1.0-1jpp.1
- Import from JPackage
- Update per Fedora spec

* Wed Nov 14 2007 Ralph Apel <r.apel @ r-apel.de> - 0:1.0-1jpp
- Initial build
