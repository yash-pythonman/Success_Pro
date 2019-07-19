import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HomepageimageComponent } from './homepageimage.component';

describe('HomepageimageComponent', () => {
  let component: HomepageimageComponent;
  let fixture: ComponentFixture<HomepageimageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HomepageimageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HomepageimageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
